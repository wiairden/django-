# models.py
from django.db import models


##用户id 用户账户 密码 手机号 年龄
class userinfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=64)
    user_number = models.IntegerField()
    user_age = models.IntegerField(default=2)
##任务id 任务名称 发布用户id 发布用户名称 发布日期 截止日期 接收用户id 接收用户名称 接收日期 是否接取状态 是否为完成状态
class rw(models.Model):
    rw_id = models.AutoField(primary_key=True)
    rw_name = models.CharField(max_length=20)
    rw_context = models.CharField(max_length=40)
    rw_fb_userid = models.ForeignKey(userinfo,related_name='userinfo_fb_set',on_delete=models.CASCADE)
    rw_fb_username = models.CharField(max_length=20)
    rw_startdata = models.CharField(max_length=20)
    rw_enddata = models.CharField(max_length=20)
    rw_js_userid =  models.ForeignKey(userinfo, related_name='userinfo_js_set',on_delete=models.CASCADE,null=True)
    rw_js_username = models.CharField(max_length=20,null=True)
    rw_js_data = models.CharField(max_length=20,null=True)
    rw_js_state = models.BooleanField(default=False)
    rw_state = models.BooleanField(default=False)