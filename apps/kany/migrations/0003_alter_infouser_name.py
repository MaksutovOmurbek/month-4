# Generated by Django 5.0.2 on 2024-03-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kany', '0002_alter_infouser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]
