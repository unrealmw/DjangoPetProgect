from django.db import models


class Worker(models.Model):
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    birth_date = models.DateField("Дата рождения",)
