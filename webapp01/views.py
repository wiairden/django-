from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp01.models import userinfo,rw
from webapp01 import models
from django.db.models import Q
from django import forms
from datetime import datetime, timedelta
import hashlib

class LoginForm(forms.Form):
    user_name=forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    user_password=forms.CharField(
        label="用户名",
        widget=forms.PasswordInput,
        required=True
    )
    errror = ""
    

# Create your views here.
def hello(request):
    return HttpResponse("Hello ")
##添加用户
def user_add(request):
    if request.method=="POST":
        form = LoginForm()
        user_name1 = request.POST.get('user_name')
        user_password1 = request.POST.get('user_password')
        user_number1 = request.POST.get('user_number')
        user_age1 = request.POST.get('user_age')
        username = userinfo.objects.filter(user_name=user_name1).first()
        if username is not None :
            if user_name1 == username.user_name :
                form.error = "该用户名已被注册！"
                return render(request,"user_add.html",{'form':form})
        else:
            userinfo.objects.create(user_name=user_name1,user_password=user_password1,user_number=user_number1,user_age=user_age1)
            return redirect("http://127.0.0.1:8000")
    return render(request,"user_add.html")

##用户界面
def userinfo1(request):
    rw_list = userinfo.objects.all()
    return render(request,"userinfo.html",{'rw_list':rw_list})


##主页
def welcome(welcome):
    rw_list = rw.objects.filter(rw_js_state=False)
    login = False
    return render(welcome,"welcome.html",{'rw_list':rw_list,'login':login})


def insert(request):
    books = models.userinfo.objects.create(user_name="wiair",user_password=123,user_number=123344)
    return redirect("http://127.0.0.1:8000/userinfo")


##删除用户
def delete(request):
    user_id1 = request.GET.get('user_id')
    print(user_id1)
    models.userinfo.objects.filter(user_id = user_id1).delete()
    return redirect("http://127.0.0.1:8000/userinfo")


##删除任务
def rw_delete(request):
    rw_id1 = request.GET.get('rw_id')
    print(rw_id1)
    models.rw.objects.filter(rw_id = rw_id1).delete()
    return redirect("http://127.0.0.1:8000/task/mytask")



##md5加密
def clean_user_password(password):
        Encry = hashlib.md5()  # 实例化md5
        Encry.update(password.encode())  # 字符串字节加密
        md5_pwd = Encry.hexdigest() # 字符串加密
        return md5_pwd



##用户登录模块
def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,"user_login.html",{'form':form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # yz = models.userinfo.objects.filter(user_name = form.cleaned_data['user_name'],user_password = form.cleaned_data['user_password']).first()
        #如果数据库字段一致可以用以下写法
        yz = models.userinfo.objects.filter(**form.cleaned_data).first()
        # print(form.cleaned_data['user_name'],clean_user_password(form.cleaned_data['user_password']))
        # print(yz)
        if not yz:
            form.error=("用户名或密码错误！")
            return render(request,"user_login.html",{'form':form})
        else:
            request.session["info"] = {'id':yz.user_id,'name':yz.user_name}
            # print(request.session["info"]['id'])
            # print(request.session["info"]['id'])
            rw_list1 = rw.objects.filter(rw_js_state = False)
            return redirect("http://127.0.0.1:8000/login_success",{'name1':request.session["info"],'rw_list':rw_list1})
    else:
        form.error=("不能为空!")
        return render(request,"user_login.html",{'form':form})
##登录成功页面
def login_success(request):
    rw_user = request.session.get('info')
    rw_list1 = rw.objects.filter(Q(rw_js_state = False) & Q(rw_state=False))
    return render(request,"login_success.html",{'name1':rw_user,'rw_list':rw_list1})

##添加任务页面
def task_add(request):
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    time1 = f"{year}年{month}月{day}日{hour}时"
    current_time2 = current_time + timedelta(days=1)
    year = current_time2.year
    month = current_time2.month
    day = current_time2.day
    hour = current_time2.hour
    time2 = f"{year}年{month}月{day}日{hour}时"

    if request.method=="POST":
        rw_user = request.session.get('info')
        rw_name1 = request.POST.get('rw_name')
        rw_context1 = request.POST.get('rw_context')
        rw_startdata1 = request.POST.get('rw_fb_startdata')
        rw_enddata1 = request.POST.get('rw_fb_enddata')
        rw.objects.create(
            rw_name=rw_name1,
            rw_fb_username=rw_user.get('name'),
            rw_fb_userid=rw_user.get('id'),
            rw_startdata=rw_startdata1,
            rw_enddata=rw_enddata1,
            rw_context=rw_context1,
            )
        return redirect("http://127.0.0.1:8000/login_success")
    return render(request,"task_add.html",{"time1":time1,"time2":time2})
##我的任务页面
def task_mytask(request):
    rw_user = request.session.get('info')
    rw_fb_username1=rw_user.get('name'),
    rw_list1 = rw.objects.filter(rw_fb_username=rw_fb_username1[0])
    rw_list2 = rw.objects.filter(Q(rw_js_username=rw_fb_username1[0]) & Q(rw_state=False))
    return render(request,"task_mytask.html",{'rw_list':rw_list1,'rw_jslist':rw_list2})
##任务详情页
def task_detail(request):
    rw_id1 = request.GET.get('rw_id')
    login1 = request.GET.get('login')
    print(login1)
    rw1 = rw.objects.filter(rw_id=rw_id1)
    return render(request,"task_detail.html",{"rw_detail":rw1,"login":login1})
##注销
def clear_session(request):
    request.session.clear()
    return redirect("http://127.0.0.1:8000/")
##接收任务
def js_rw(request):
    rw_id1 = request.GET.get('rw_id')
    rw.objects.filter(rw_id = rw_id1).update(rw_js_state = "True")
    rw_user = request.session.get('info')
    rw_js_username1=rw_user.get('name')
    rw_js_userid1=rw_user.get('id')
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    rw_js_data1 = f"{year}年{month}月{day}日{hour}时"
    rw.objects.filter(rw_id = rw_id1).update(
        rw_js_userid_id = rw_js_userid1,
        rw_js_username = rw_js_username1,
        rw_js_data = rw_js_data1,
    )
    # +类.objects.create(+列="内容")
    ##+类.objects.filter(+列="内容"(查找的内容)).update("修改的内容")
    return redirect("http://127.0.0.1:8000/login_success")
##删除接收任务
def del_js_rw(request):
    rw_id1 = request.GET.get('rw_id')
    rw_js_username1=None
    rw_js_userid1=None
    rw_js_data1 =None
    rw.objects.filter(rw_id = rw_id1).update(rw_js_state = "False")
    rw.objects.filter(rw_id = rw_id1).update(
        rw_js_userid_id = rw_js_userid1,
        rw_js_username = rw_js_username1,
        rw_js_data = rw_js_data1,
    )
    rw_user = request.session.get('info')
    rw_fb_username1=rw_user.get('name'),
    rw_list1 = rw.objects.filter(rw_fb_username=rw_fb_username1[0])
    rw_list2 = rw.objects.filter(rw_js_username=rw_fb_username1[0])
    return render(request,"task_mytask.html",{'rw_list':rw_list1,'rw_jslist':rw_list2})
##完成任务
def wc_rw(request):
    rw_id1 = request.GET.get('rw_id')
    rw.objects.filter(rw_id = rw_id1).update(rw_state = "True")
    rw_user = request.session.get('info')
    rw_fb_username1=rw_user.get('name'),
    rw_list1 = rw.objects.filter(rw_fb_username=rw_fb_username1[0])
    rw_list2 = rw.objects.filter(rw_js_username=rw_fb_username1[0])
    return redirect("http://127.0.0.1:8000/task/mytask",{'rw_list':rw_list1,'rw_jslist':rw_list2})
##搜索功能
def search1(request):
    if request.method=="POST":
        login1 = request.GET.get('login')
        search = request.POST.get('search')
        print(request.POST.get('search'))
        rw_search1 = rw.objects.filter(rw_name=search)
        user_search1 = rw.objects.filter(rw_fb_username=search)
        return render(request,"search1.html",{'rw_search': rw_search1,'user_search':user_search1,'login':login1})
    else:
        return HttpResponse("ERROR!请使用POST方法访问内容")
