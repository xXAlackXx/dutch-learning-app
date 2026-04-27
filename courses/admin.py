from django.contrib import admin
from .models import Level, Unit, Lesson, Vocabulary, LessonVocabulary
# Register your models here.
admin.site.register(Level)
admin.site.register(Unit)
admin.site.register(Lesson)
admin.site.register(Vocabulary)
admin.site.register(LessonVocabulary)
