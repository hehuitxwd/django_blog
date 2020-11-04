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

##文章分类
class Category(models.Model):
    name = models.CharField('博客分类',max_length=100)
    index = models.IntegerField(default=999,verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#文章标签
class Tag(models.Model):
    name = models.CharField('文章标签',max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

##推荐位
class Tui(models.Model):
    name = models.CharField('推荐位',max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


##banner位
class Banner(models.Model):
    text_info = models.CharField('标题',max_length=50,default='')
    img = models.ImageField('轮播图',upload_to='banner/')
    link_url = models.URLField('图片链接',max_length=100)
    is_active = models.BooleanField('是否是active',default=False)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info

#友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'

