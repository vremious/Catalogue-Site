# Generated by Django 4.1.5 on 2023-09-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_employee_options_filtermix1'),
    ]

    operations = [
        migrations.AddField(
            model_name='filtermix1',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
