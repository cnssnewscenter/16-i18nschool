from django.db import models
from ckeditor.fields import RichTextField
from pyquery import PyQuery as pyquery

class News(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField()
    content = RichTextField()

    def get_pic(self):
        items = pyquery(self.content).find('img')
        if items:
            return items[0].attrib['src']
        else:
            return None

    def get_intro(self):
        post = pyquery(self.content).text()
        return post[:250]


class Teacher(models.Model):
    pic = models.ImageField(upload_to="teacher", blank=True)
    name = models.CharField(max_length=256)
    course = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    school_own = models.CharField(max_length=256)
    intro = RichTextField()
    teacher_intro = RichTextField()
    def image_(self):
        return '<a href="/media/{0}"><img src="/media/{0}"></a>'.format(self.pic)
    image_.allow_tags = True

    def __str__(self):
        return self.course + '|' + self.name



