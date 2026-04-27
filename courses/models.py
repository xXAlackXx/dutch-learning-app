from django.db import models

# Create your models here.

class Level(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    order = models.IntegerField()
    
    def __str__(self):
        return self.name


class Unit(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()
    difficulty = models.CharField(max_length=20, 
                                  choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    words = models.ManyToManyField('Vocabulary', through='LessonVocabulary')

    def __str__(self):
        return self.title

class Vocabulary(models.Model):
    dutch_text = models.CharField(max_length=50)
    translation = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=20, 
                            choices=[('word', 'Word'), ('digraph', 'Digraph')])
    pronunciation_audio = models.CharField(max_length=250)

    def __str__(self):
        return self.dutch_text
    
    class Meta:
        verbose_name_plural = "Vocabularies"

class LessonVocabulary(models.Model): 
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    role = models.CharField(max_length=20,
                            choices=[('main', 'Main'), ('example', 'Example')])
    order = models.IntegerField()
    
    def __str__(self):
        return f"{self.lesson.title} - {self.vocabulary.dutch_text} ({self.role})"
    
    class Meta:
        verbose_name_plural = "Lesson Vocabularies"