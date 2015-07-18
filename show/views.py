from django.shortcuts import render
from .models import Teacher, News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404

def index(request):
    teachers = Teacher.objects.all()
    news = [i for i in News.objects.all() if i.get_pic()][:5]
    print(news)
    return render(request, "index.html", dict(teachers=teachers, news=news))


def news(request):
    newses = News.objects.all()
    pages = Paginator(newses, 25)
    page = request.GET.get('page')
    try:
        contents = pages.page(page)
    except PageNotAnInteger:
        contents = pages.page(1)
    except EmptyPage:
        contents = pages.page(pages.num_pages)
    return render(request, "news.html", dict(content=contents))


def single_passage(request, pid):
    contents = News.objects.all().reverse()[:10]
    try:
        post = News.objects.get(pk=pid)
        return render(request, "single.html", dict(post=post, posts=contents))
    except:
        raise Http404
