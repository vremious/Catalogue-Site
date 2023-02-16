# Generated by Django 4.1.5 on 2023-02-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_models_type_alter_router_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='models',
            options={'verbose_name': 'Оборудование', 'verbose_name_plural': 'Оборудование'},
        ),
        migrations.AlterModelOptions(
            name='scooter',
            options={'verbose_name': 'Электросамокат', 'verbose_name_plural': 'Электросамокаты'},
        ),
        migrations.AlterModelOptions(
            name='vacuum',
            options={'verbose_name': 'Робот-пылесос', 'verbose_name_plural': 'Роботы-пылесосы'},
        ),
        migrations.AlterField(
            model_name='router',
            name='wifi_freq',
            field=models.CharField(choices=[('2,4', '2,4 ГГц'), ('2,4/5', '2,4/5 ГГц'), ('-', 'Нет')], max_length=50, verbose_name='Диапазон Wi-Fi'),
        ),
    ]
