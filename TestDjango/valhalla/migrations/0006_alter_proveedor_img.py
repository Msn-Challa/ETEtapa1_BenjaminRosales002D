# Generated by Django 3.2.3 on 2021-07-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valhalla', '0005_alter_proveedor_moneda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='img',
            field=models.ImageField(null=True, upload_to='', verbose_name='Logo de proveedor'),
        ),
    ]