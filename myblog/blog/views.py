from django.shortcuts import render
from django.http import HttpResponse
from blog import models
# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse('欢迎使用Django！')

def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    content = {
        'blog_index':blog_index
    }
    return render(request,'index.html',content)