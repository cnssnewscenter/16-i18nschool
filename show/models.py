from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField()
    content = RichTextField()


class Teacher(models.Model):
    pic = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    intro = RichTextField()


class Courses(models.Model):
    name = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    school_own = models.CharField(max_length=256)
    intro = RichTextField()
