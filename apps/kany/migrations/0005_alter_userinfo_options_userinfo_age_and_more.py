# Generated by Django 5.0.2 on 2024-03-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kany', '0004_userinfo_delete_infouser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'Пользовательская', 'verbose_name_plural': 'Пользовательская'},
        ),
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=1, verbose_name='Возраст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='facebook',
            field=models.URLField(default=1, verbose_name='Facebook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default=1, upload_to='Image', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='instagram',
            field=models.URLField(default=1, verbose_name='Instagram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='job',
            field=models.CharField(default=1, max_length=255, verbose_name='работа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='telegram',
            field=models.URLField(default=1, verbose_name='Telegram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='whatsapp',
            field=models.URLField(default=1, verbose_name='Whatsapp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='youtube',
            field=models.URLField(default=1, verbose_name='YouTube'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Фамилмя'),
        ),
    ]