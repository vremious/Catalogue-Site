# Generated by Django 4.1.5 on 2023-08-09 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='type_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.type', verbose_name='Тип оборудования'),
            preserve_default=False,
        ),
    ]