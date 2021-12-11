from django.db import models
from django import forms
import hashlib


# Create your models here.

class AuthUser(models.Model):
    user_name = models.CharField(max_length=20, name="用户名", verbose_name="用户名", null=False, unique=True)
    login_name = models.CharField(max_length=20, verbose_name="登录账号", null=False, unique=True)
    e_mail = models.CharField(max_length=20, verbose_name="邮箱", null=True, unique=True)
    password = models.CharField(max_length=20, verbose_name="密码")
    last_login = models.DateTimeField(null=True)
    # 逻辑删除标识字段
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "用户"
        verbose_name = "用户"
        db_table = "user"

    # def save(self, *args, **kwargs):
    #     md5 = hashlib.md5()
    #     md5.update(self.password.encode())
    #     super(AuthUser, self).save(*args, **kwargs)
    #
    # def md5(self, pwd):
    #     md5 = hashlib.md5()
    #     md5.update(pwd.encode())
    #     saltpassword = md5.hexdigest()
    #     return saltpassword
    #
    # def sha1(key):
    #     sha1_key = hashlib.sha1()
    #     sha1_key.update(key.encode("utf-8"))
    #     return sha1_key.hexdigest()
