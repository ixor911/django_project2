from django.db import models


class Task(models.Model):
    name = models.CharField('Name', max_length=50)
    task = models.TextField('Task')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'task1'
        verbose_name_plural = 'tasks1'


