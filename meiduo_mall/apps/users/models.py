from django.db import models

# Create your models here.


# 1.自己定义模型类
# 密码要加密，登陆时要进行验证
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=11, unique=True)


# 2.django自带的用户模型类
# 这个用户模型类 有密码加密 和 密码的验证
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     mobile = models.CharField(max_length=11, unique=True)
#
#     class Meta:
#         db_table = 'tb_users'
#         verbose_name = '用户管理'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username
