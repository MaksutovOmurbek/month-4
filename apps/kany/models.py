from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(
        max_length = 255, 
        verbose_name = 'Имя')
    
    last_name = models.CharField(
    max_length = 255, 
    verbose_name = 'Фамилмя')

    job = models.CharField(
    max_length = 255, 
    verbose_name = 'работа')

    image = models.ImageField(
    upload_to='Image', 
    verbose_name= 'Фото')\
    
    description = models.TextField(
    verbose_name = 'Описание')

    age = models.IntegerField(
    verbose_name = 'Возраст')

    email = models.EmailField(
    verbose_name = 'email')

    youtube = models.URLField(
    verbose_name = 'YouTube')

    instagram = models.URLField(
    verbose_name = 'Instagram')

    whatsapp = models.URLField(
    verbose_name = 'Whatsapp')

    telegram = models.URLField(
    verbose_name = 'Telegram')

    facebook = models.URLField(
    verbose_name = 'Facebook')

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользовательская'
        verbose_name_plural = 'Пользовательская'

class Education(models.Model):
    year = models.IntegerField(
            verbose_name = 'Год',
        )

    title = models.CharField(
            max_length = 255,
            verbose_name = 'название'
        )

    descrip = models.TextField(
            verbose_name = 'Описание'
        )

        
    def __str__(self) -> str:
        return f"{self.title}"
    

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

class Experience(models.Model):
    year = models.IntegerField(
            verbose_name = 'Год',
        )

    title = models.CharField(
            max_length = 255,
            verbose_name = 'название'
        )

    descrip = models.TextField(
            verbose_name = 'Описание'
        ) 

    def __str__(self) -> str:
        return f"{self.title}"
    

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт' 


class Blog(models.Model):
    data = models.DateField(
            verbose_name = 'Дата',
        )

    image = models.ImageField(
            verbose_name = 'Фото'
        )

    descrip = models.TextField(
            verbose_name = 'Описание'
        ) 
    title = models.CharField(
            max_length = 255,
            verbose_name = 'название'
        )

    def __str__(self) -> str:
        return f"{self.title}"
    

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог' 

class Skills (models.Model):
    pronc = models.IntegerField(
        verbose_name = 'Процент'
    )

    title = models.CharField(
        max_length = 255,
         verbose_name = 'Название'
    )

    
    def __str__(self) -> str:
        return f"{self.title}"
    

    
    class Meta:
        verbose_name = 'Скилы'
        verbose_name_plural = 'Скилы' 
