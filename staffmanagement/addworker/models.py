from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название")
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Места работы"
        verbose_name = 'Место работы'
        ordering = ['-name']


class Worker(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30)
    birth_date = models.DateField(verbose_name="Дата рождения",)
    department = models.ForeignKey('Department', null=True, on_delete=models.PROTECT, verbose_name="Место работы")
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Данные работника"
        verbose_name = 'Данные работника'
        ordering = ["pk"]



