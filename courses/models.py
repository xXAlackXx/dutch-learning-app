from django.db import models

# Create your models here.

class Level(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    order = models.IntegerField()


class Unit(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.PROTECT)

class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()
    difficulty = models.CharField(max_length=20, 
                                  choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])