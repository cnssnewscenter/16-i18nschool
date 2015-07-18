from django.shortcuts import render
from .models import Teacher, News


def index(request):
    teachers = Teacher.objects.all()
    news = [i for i in News.objects.all() if i.get_pic()][:5]
    print(news)
    return render(request, "index.html", dict(teachers=teachers, news=news))


def news(self):
    return render("news.html")


def single_passage(self, pid):
    return render("single.html")
