from django.db import models


# Create your models here.


class GuestReview(models.Model):
    STATUS_CHOICES = (
        ('active', 'Активно'),
        ('blocked', 'Заблокировано')
    )
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(unique=True, verbose_name='Email')
    description = models.TextField(max_length=3000, verbose_name='Запись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время редактирования')
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f'{self.author} ({self.email})'
