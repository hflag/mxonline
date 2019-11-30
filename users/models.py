from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,
                                 verbose_name='昵称',
                                 default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=8, choices=(('male', '男'), ('female', '女')), default='female')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/$m')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(verbose_name='邮箱')
    send_type = models.CharField(max_length=20, choices=(('register', '注册'), ('forget', '找回密码')))
    send_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='邮箱验证'
        verbose_name_plural=verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
