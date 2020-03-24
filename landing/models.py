from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return "Пользователь %s, %s." % (self.name, self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
