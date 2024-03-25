# Generated by Django 5.0.2 on 2024-03-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kany', '0003_alter_infouser_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Информации пользователя',
            },
        ),
        migrations.DeleteModel(
            name='InfoUser',
        ),
    ]