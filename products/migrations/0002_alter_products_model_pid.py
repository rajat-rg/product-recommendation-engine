# Generated by Django 3.2.6 on 2021-08-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_model',
            name='PID',
            field=models.CharField(max_length=255),
        ),
    ]
