from django.shortcuts import render
from .models import Teacher, Courses


def index(self):
    teachers = Teacher.objects.all()
    posts = Courses.objects.reverse()[:5]
    return render("index.html", posts=posts, teachers=teachers)


def news(self):
    return render("news.html")


def single_passage(self, pid):
    return render("single.html")
