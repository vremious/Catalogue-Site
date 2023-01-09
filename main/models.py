from django.db import models



class Service(models.Model):
    service_centre = models.CharField(max_length=250, verbose_name='Сервисные центры')

    def __str__(self):
        return self.service_centre


class Purpose(models.Model):
    purpose = models.CharField(max_length=250, verbose_name='Назначение оборудования', choices=(
         ('На продажу', 'На продажу'),
         ('Абонентское', 'Абонентское')
    ))

    def __str__(self):
        return self.purpose


class Models(models.Model):
    model = models.CharField(max_length=50, verbose_name='Модель оборудования')
    type = models.CharField(max_length=50, verbose_name='Вид оборудования', choices=(
        ("Модемы", "Модемы"),
        ("Zala", "Zala"),
        ("Умный Дом", "Умный Дом"),
        ("Телевизоры", "Телевизоры"),
        ("Ноутбуки", "Ноутбуки"),
        ("Планшеты", "Планшеты"),
        ("Умные часы", "Умные часы"),
        ("Электросамокаты", "Электросамокаты"),
        ("Роботы пылесосы", "Роботы пылесосы"),
        ("Кофе-машины", "Кофе-машины"),
        ("Кондиционеры", "Кондиционеры"),
        ("Умные колонки", "Умные колонки"),
        ("Прочее оборудование", "Прочее оборудование")
    ))

    def __str__(self):
        return self.model


class Router(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    type = models.CharField(max_length=50,  choices=(
         ('ADSL', 'ADSL'),
         ('VDSL', 'VDSL'),
         ('PON', 'PON'),
         ('SALE', 'SALE')
    ), verbose_name="Тип модема")
    company = models.CharField(max_length=50, verbose_name='Производитель')
    wifi = models.CharField(max_length=50, verbose_name='Наличие Wi-Fi', choices=(
         ('+', '+'),
         ('-', '-')
    ))
    wifi_freq = models.CharField(max_length=50, verbose_name='Диапазон Wi-Fi', choices=(
         ('2,4', '2,4'),
         ('2,4/5', '2,4/5'),
         ('-', '-')
    ))
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')
    image = models.ImageField(upload_to='main/media', blank=True, null=True)


    def __str__(self):
        return str(self.model)


class Zala(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    type = models.CharField(max_length=50, verbose_name="Тип оборудования", choices=(
        ('IPTV', 'IPTV'),
        ('Эфирная', 'Эфирная'),
    ))
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class SmartHome(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    type = models.CharField(max_length=50, verbose_name="Тип оборудования")
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class Tv(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    size = models.FloatField(max_length=4, verbose_name="Диагональ экрана")
    resolution = models.CharField(max_length=20, verbose_name='Разрешение экрана')
    smart = models.CharField(max_length=40, verbose_name="Наличие SmartTV")
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class Notebook(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    size = models.FloatField(max_length=4, verbose_name="Диагональ экрана")
    cpu = models.CharField(max_length=20, verbose_name='Модель процессора')
    ddr = models.PositiveSmallIntegerField(verbose_name='Объём оперативной памяти')
    memory = models.CharField(max_length=20, verbose_name='Вид и объём накопителя')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class Pad(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    size = models.FloatField(max_length=4, verbose_name="Диагональ экрана")
    ddr = models.PositiveSmallIntegerField(verbose_name='Объём оперативной памяти')
    memory = models.PositiveSmallIntegerField(verbose_name='Объём накопителя')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class Watch(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    size = models.FloatField(max_length=4, verbose_name="Диагональ экрана")
    os = models.CharField(max_length=50, verbose_name='Операционная система')
    support = models.CharField(max_length=50, verbose_name='Поддержка платформ')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')
    image = models.ImageField(upload_to='main/media', blank=True, null=True)

class Scooter(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class Vacuum(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    maxspeed = models.CharField(max_length=50, verbose_name='Максимальная скорость и дистанция')
    power = models.CharField(max_length=50, verbose_name='Мощность мотора')
    accumulator = models.CharField(max_length=50, verbose_name='Аккумулятор')
    maxload = models.CharField(max_length=50, verbose_name='Максимальная нагрузка')
    weight = models.CharField(max_length=50, verbose_name='Вес')
    chargetime = models.CharField(max_length=50, verbose_name='Время заряда')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class Coffee(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    type = models.CharField(max_length=50, verbose_name="Тип оборудования")
    pressure = models.PositiveSmallIntegerField(verbose_name='Давление (Бар)')
    capucinator = models.CharField(max_length=50, verbose_name='Тип капучинатора', choices=(
        ('Ручной', 'Ручной'),
        ('Автоматичесий', 'Автоматичесий')
    )
    )
    control = models.CharField(max_length=50, verbose_name='Управление', choices=(
        ('Механическое', 'Механическое'),
        ('Электронное', 'Электронное'),
        ('Сенсорное', 'Сенсорное')
    )
    )
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')



class Conditioner(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    conditioner_type = models.CharField(max_length=50, verbose_name='Тип кондиционера')
    power = models.CharField(max_length=50, verbose_name='Мощность охлаждения/обогрева ')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class SmartSpeaker(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    company = models.CharField(max_length=50, verbose_name='Производитель')
    bluetooth = models.CharField(max_length=50, verbose_name='Версия Bluetooth')
    power = models.CharField(max_length=50, verbose_name='Номинальная мощность')
    control = models.CharField(max_length=50, verbose_name='Управление')

class Other(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    type = models.CharField(max_length=50, verbose_name="Тип оборудования")
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Назначение')


class Available(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель оборудования')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Сервисный центр')
    available = models.CharField(max_length=20, verbose_name="Наличие", choices=(
         ('+', '+'),
         ('-', '-')
    ))
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    date = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        ordering = ['model']

    def __str__(self):
        return str(f'{self.service}-{self.model}-{self.available}-{self.quantity}')

class Category_abon(models.Model):
    name_cat = models.CharField(max_length=250)

    def __str__(self):
        return self.name_cat


class Subcategory(models.Model):
    cat = models.ForeignKey(Category_abon, on_delete=models.CASCADE,
                            verbose_name='')
    name_subcat = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.cat} - {self.name_subcat}'


class Good(models.Model):
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                               verbose_name='subcategory')
    name_good = models.CharField(max_length=250)


    def __str__(self):
         return f'{self.subcat} - {self.name_good}'


class State(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='service center')
    name_good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='good')
    date = models.DateTimeField("Дата обновления", auto_now=True)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=(
         ('+', '+'),
         ('-', '-')
    ))

    class Meta:
        ordering = ['name_good']

    def __str__(self):
        return f'{self.service} - {self.name_good} - {self.status}- {self.quantity}'


class OrderItem(models.Model):
    order = models.ForeignKey("main.Order", on_delete=models.CASCADE, verbose_name="order")
    cat = models.ForeignKey(Category_abon, on_delete=models.CASCADE, verbose_name='cat')
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='subcat')
    name_good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='good')
    quantity = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.name_good} + {self.quantity}'




class Order(models.Model):
    order_id = models.PositiveIntegerField(unique=True)
    order_date = models.DateTimeField(auto_now=True)
    total_quantity = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.order_id)


class AllowedCombination(models.Model):
    cat = models.ForeignKey(Category_abon, on_delete=models.CASCADE)
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cat} {self.subcat} {self.good}'

    class Meta:
        ordering = ['pk']
