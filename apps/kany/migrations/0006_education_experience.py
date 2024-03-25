# Generated by Django 5.0.2 on 2024-03-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kany', '0005_alter_userinfo_options_userinfo_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('descrip', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образование',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('descrip', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Опыт',
                'verbose_name_plural': 'Опыт',
            },
        ),
    ]
