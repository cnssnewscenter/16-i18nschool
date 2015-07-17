from django.shortcuts import render
from .models import Teacher, News


def index(request):
    teachers = Teacher.objects.all()
    news = News.objects.all()
    return render(request, "index.html", dict(teachers=teachers))


def news(self):
    return render("news.html")


def single_passage(self, pid):
    return render("single.html")
