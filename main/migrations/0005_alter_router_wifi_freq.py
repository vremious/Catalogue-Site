# Generated by Django 4.1.5 on 2023-02-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_models_options_alter_scooter_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='wifi_freq',
            field=models.CharField(choices=[('2,4 Ггц', '2,4'), ('2,4/5', '2,4/5'), ('-', '-')], max_length=50, verbose_name='Диапазон Wi-Fi'),
        ),
    ]
