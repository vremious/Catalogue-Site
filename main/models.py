from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from transliterate import translit
from django.contrib.auth.models import User


class Purpose(models.Model):
    purpose = models.CharField(max_length=250, verbose_name='Назначение оборудования', choices=(
        ('На продажу', 'На продажу'),
        ('Абонентское', 'Абонентское')
    ))

    class Meta:
        verbose_name = 'Назначение оборудования'
        verbose_name_plural = 'Назначение оборудования'

    def __str__(self):
        return self.purpose


class Company(models.Model):
    company = models.CharField(max_length=50, verbose_name='Производитель', unique=True)

    class Meta:
        verbose_name = 'Производитель оборудования'
        verbose_name_plural = 'Производитель оборудования'
        ordering = ['company']

    def __str__(self):
        return self.company


class Type(models.Model):
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=50, verbose_name='Тип оборудования', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', null=True, blank=True, editable=False)

    def my_slugify(self):
        return slugify(translit(self.type, 'ru', reversed=True))

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == 'slug':
            self.slug = self.my_slugify()
        super(Type, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Тип оборудования'
        ordering = ['type']

    def __str__(self):
        return str(self.type)


class Service(models.Model):
    service_centre = models.CharField(max_length=250, verbose_name='Сервисные центры')

    class Meta:
        verbose_name = 'Сервисный центр'
        verbose_name_plural = 'Сервисные центры'

    def __str__(self):
        return self.service_centre


class AddFilterName1(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название параметра фильтра',
                            blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Название фильтра'
        verbose_name_plural = 'Названия фильтра'

    def __str__(self):
        return self.name


class AddFilter1(models.Model):
    value = models.CharField(max_length=50, verbose_name='Параметр фильтра',
                             blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Значение фильтра'
        verbose_name_plural = 'Значения фильтра'

    def __str__(self):
        return self.value


class Models(models.Model):
    type_fk = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип оборудования')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Производитель')
    model = models.CharField(max_length=50, verbose_name='Модель оборудования')
    actual = models.CharField(max_length=3, verbose_name='Актуально', choices=(
        ('Да', 'Да'),
        ('Нет', 'Нет')
    ), default='Да')
    add_filter_name = models.ForeignKey(AddFilterName1, on_delete=models.CASCADE,
                                        verbose_name='Название дополнительного фильтра', blank=True, null=True)
    add_filter = models.ForeignKey(AddFilter1, on_delete=models.CASCADE, verbose_name='Значение фильтра',
                                   blank=True, null=True)

    def photo_upload(self, filename):
        return f'main/media/{self.type_fk.slug}/{filename}'

    #
    image = models.ImageField(upload_to=photo_upload, blank=True, null=True)
    price = models.FloatField(verbose_name='Стоимость', blank=True, null=True)
    split_period = models.IntegerField(verbose_name='Период рассрочки', blank=True, null=True)

    def split_price(self):
        if self.price%self.split_period == 0:
            return round(self.price//self.split_period, 0)
        else:
            return round(self.price/self.split_period, 2)

    #
    # # Функция для создания подкаталогов медиа по типу устройств, для запуска раскоментить,
    # # в терминале вызвать модель Model,
    # # запусить цикл с параметром .save()
    # def save(self, *args, **kwargs):
    #     super(Models, self).save(*args, **kwargs)
    #     if self.image.name:
    #         image_name = str(os.path.split(self.image.name)[-1])
    #         if self.image:
    #             initial_path = self.image.path
    #             if f'{self.type_fk.slug}' in self.image.path:
    #                 pass
    #             else:
    #                 if not os.path.exists(f'main/media/{self.type_fk.slug}'):
    #                     os.makedirs(f'main/media/{self.type_fk.slug}')
    #                 new_path = os.path.join('C:\\Users\\Denis\\PycharmProjects\\Catalgue_v2\\main\\media\\',
    #                                         self.type_fk.slug, image_name)
    #                 new_name = f'main/media/{self.type_fk.slug}/{image_name}'
    #                 shutil.copyfile(initial_path, new_path)
    #                 # os.rename(initial_path, new_path)
    #                 self.image.name = new_name
    #                 super(Models, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        unique_together = ('company', 'model')

    def __str__(self):
        return self.model


class Available(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Сервисный центр')
    available = models.CharField(max_length=20, verbose_name="Наличие", choices=(
        ('+', '+'),
        ('-', '-')
    ), default='-')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество', default='0')
    date = models.DateTimeField("Дата обновления", auto_now=True)

    def clean(self):
        cleaned_data = super().clean()
        if self.available == '-' and self.quantity != 0:
            raise ValidationError({'available': ['Исправьте значение на "+"']})
        elif self.available == '+' and self.quantity == 0:
            raise ValidationError({'available': ['Исправьте значение на "-"']})

    class Meta:
        ordering = ['model']
        verbose_name = 'Наличие оборудования'
        verbose_name_plural = 'Наличие оборудования'
        unique_together = ('service', 'model')

    def __str__(self):
        return str(f'{self.service}-{self.model}-{self.available}-{self.quantity}')


# Декоратор, который автоматизирует создание "наличие оборудования" на всех СЦ, при создании нового оборудования:
@receiver(post_save, sender=Models)
def create_new_available_objects(instance, created, **kwargs):
    for service_id in Service.objects.values_list('id', flat=True):
        if not Available.objects.filter(model=instance, service_id=service_id):
            Available.objects.create(model=instance, service_id=service_id, available='-', quantity=0)
        else:
            pass


class TesterTime(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Сервисный центр')
    worktime = models.TextField(max_length=150, verbose_name='Время работы тестировщика')
    onduty = models.BooleanField(verbose_name='Тестировщик на месте')
    date = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = 'Время работы тестировщика'
        verbose_name_plural = 'Время работы тестировщика'

    def __str__(self):
        return str(f'{self.service}---------{self.worktime}----------{self.onduty}')


#Декоратор автоматически добавлюящий "Время работы тестировщика" при добавлении нового СЦ:
@receiver(post_save, sender=Service)
def create_new_available_testertime(instance, created, **kwargs):
    for service_id in Service.objects.values_list('id', flat=True):
        if not TesterTime.objects.filter(service=instance):
            TesterTime.objects.create(service=instance, onduty=False)
        else:
            pass


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Сервисный центр',
                                null=True, blank=True)

    class Meta:
        verbose_name = "Привязка админов к СЦ"
        verbose_name_plural = 'Привязки админов к СЦ'

    def __str__(self):
        return str(f'{self.user} - {self.service}')


#Декоратор добавляющий и убирающий оборудование взависимотси от актуальности:
@receiver(post_save, sender=Available)
def change_actual(**kwargs):
    for m in Models.objects.filter(type_fk__purpose=1).values_list('id', flat=True):
        if Available.objects.filter(model=m, available='+'):
            Models.objects.filter(id=m).update(actual='Да')
        elif Available.objects.filter(model=m, available='-'):
            Models.objects.filter(id=m).update(actual='Нет')

