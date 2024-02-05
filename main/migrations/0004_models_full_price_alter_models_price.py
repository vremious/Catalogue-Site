# Generated by Django 5.0a1 on 2023-12-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_company_options_alter_type_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='full_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Стоимость при единовременной оплате'),
        ),
        migrations.AlterField(
            model_name='models',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Стоимость в рассрочку'),
        ),
    ]
