# Generated by Django 5.0.2 on 2024-03-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kany', '0008_blog_alter_experience_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='data',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
