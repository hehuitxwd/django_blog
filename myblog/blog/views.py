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

#自定义400页面
# def bad_request(request):
#     return render(request,'400.html')

#自定义403错误页面
# def permission_denied(request):
#     return render(request,'403.html')

#自定义404错误页面
def page_not_found(request,exception):
    return render(request, '404_page.html')

# #自定义500错误页面
# def page_error(request):
#     return render(request,'500.html')

