from django.db import models
from django.urls import reverse
from datetime import datetime


class TaskManager(models.Manager):
    def expire_task(self):
        return self.filter(expire_date__lt=datetime.now())


class CatManager(models.Manager):
    def empty_cat(self):
        return self.filter(categories__isnull=True)

    def Full_cat(self):
        return self.exclude(categories__isnull=True)


class CategoryTask(models.Model):
    category = models.CharField(max_length=20)
    objects = CatManager()

    def __str__(self):
        return self.category


class Task(models.Model):
    PORITY_TASK = [
        (0, 'بی اهمیت'),
        (1, 'کم اهمیت'),
        (2, 'توجه'),
        (3, 'قابل توجه'),
        (4, 'مهم'),
        (5, 'ضروری'),
    ]

    title = models.CharField(max_length=250)
    # slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField()
    pority = models.IntegerField(choices=PORITY_TASK, default=4)
    category = models.ManyToManyField(CategoryTask, related_name='categories')
    expire_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TaskManager()

    class Meta:
        ordering = ["expire_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo:taskdetail', args=[str(self.id)])
