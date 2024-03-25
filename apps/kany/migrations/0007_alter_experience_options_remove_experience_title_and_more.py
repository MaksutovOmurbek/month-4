# Generated by Django 5.0.2 on 2024-03-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kany', '0006_education_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блог'},
        ),
        migrations.RemoveField(
            model_name='experience',
            name='title',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='year',
        ),
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]