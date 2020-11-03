from django.db import models
from django.contrib.auth.models import User
#导入django自带的用户模块
# Create your models here.
from django.db import models
class Article(models.Model):
    title = models.CharField('标题',max_length=100)
    body = models.TextField('内容',max_length=200,blank=True)
    create_time = models.DateTimeField('发布时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    #当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

    def __str__(self):
        return self.title