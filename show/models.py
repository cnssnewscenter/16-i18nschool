from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField()
    content = models.TextField()


class Teacher(models.Model):
    pic = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    intro = models.TextField()


class Courses(models.Model):
    name = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    school_own = models.CharField(max_length=256)
    intro = models.TextField()
