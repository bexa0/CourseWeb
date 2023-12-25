from django.db import models
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    average_time = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'pk': self.pk})


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    average_time = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.course}'

    def get_absolute_url(self):
        return reverse('module_detail', kwargs={'pk': self.pk})


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    duration_time = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.module}'

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'pk': self.pk})
