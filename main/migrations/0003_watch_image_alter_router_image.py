# Generated by Django 4.1.3 on 2023-01-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_router_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main/media'),
        ),
        migrations.AlterField(
            model_name='router',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main/media'),
        ),
    ]
