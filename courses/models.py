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
    words = models.ManyToManyField('Vocabulary', through='LessonVocabulary')

class Vocabulary(models.Model):
    dutch_text = models.CharField(max_length=50)
    translation = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=20, 
                            choices=[('word', 'Word'), ('digraph', 'Digraph')])
    pronunciation_audio = models.CharField(max_length=250)

class LessonVocabulary(models.Model): 
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    role = models.CharField(max_length=20,
                            choices=[('main', 'Main'), ('example', 'Example')])
    order = models.IntegerField()