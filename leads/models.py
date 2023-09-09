from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organizer = models.BooleanField(
        verbose_name='Организатор', default=True)
    is_agent = models.BooleanField(verbose_name='Агент', default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    organization = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, verbose_name='Организация')
    agent = models.ForeignKey(
        "Agent", null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Агент')
    category = models.ForeignKey(
        "Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления')
    phone_number = models.CharField(
        max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    # New, Contacted, Converted, Unconverted
    name = models.CharField(max_length=30, verbose_name='Название')
    organization = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Организация')

    def __str__(self):
        return self.name


class Agent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    organization = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, verbose_name='Организация')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
