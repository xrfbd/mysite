# coding=utf-8

from django.shortcuts import render_to_response, redirect,RequestContext
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Article,Label,UserProfile
from forms import NewArticleForm,LoginForm
from django import forms
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.models import User
import uuid

def index(request):

    #创建扩展用户
    #user = User.objects.get(username='admin')
    #print 'user:',user
    #profile = UserProfile.objects.create(user=user, realname='administor', email='2354@qq.com', phone=1528455784)
    #profile.save()

    if 'mysessionid_cookie' in request.COOKIES:
        session_id = request.COOKIES['mysessionid_cookie']
        username = request.session[session_id]
        return render_to_response('index.html',{'username':username})


    else:
        return render_to_response('index.html',{'username':''})

def logout(request):
    #清除cookie
    form = LoginForm(request.POST)
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('mysessionid_cookie')
    print('logout success')
    return response

def hello(request):
    return HttpResponse('hello world')

def login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #user = User.objects.filter(username=username, password=password)
            user = auth.authenticate(username = username,password = password) #使用auth认证
            if user is not None:
                #
                print('username',username)
                #response=HttpResponseRedirect(reverse('index',args=[username]))
                response = HttpResponseRedirect(reverse('index'))
                mysessionid=str(uuid.uuid4())
                response.set_cookie('mysessionid_cookie',mysessionid)
                #?????
                request.session[mysessionid] = user.username
                #
                return response
            else:
                print('form.errors',form.errors)
                return render_to_response('login.html',{'form':form,'error':form.errors})

        else:

            print('form.errors1',type(form.errors['__all__']))
            return render_to_response('login.html',{'form':form,'error':form.errors['__all__']})
    else:
        if 'mysessionid_cookie' in request.COOKIES:
            print('request.COOKIES',request.COOKIES)
            mysessionid = request.COOKIES['mysessionid_cookie']
            username = request.session[mysessionid]
            #return render_to_response('index.html',{'username':username})
            return render_to_response('index.html')

        #user=User.objects.create(username='xuran',password='111111')
        else:
            return render_to_response('login.html',{'form':form})
#x新建帖子
def edit_article(request):
    if request.method == 'POST':
        art=NewArticleForm(request.POST)
        if art.is_valid():
            print art.cleaned_data['label']
            print 'valisucceed'
            art.save()
            return HttpResponseRedirect(reverse('article_list'))
        else:
            print 'validatefail'
            raise forms.ValidationError('validate error')
            #return HttpResponse('valid fail')

    else:
        labels=Label.objects.all()
        for label in labels:
            print '%s:%s'%(label.id,label.label)
        #labels=['1','python','mysql']
        return render_to_response('new_article.html',{'labels':labels})

#帖子列表
#问题：标签显示不出来
def article_list(request):
    arts=Article.objects.all()
    for art in arts:
        for i in art.labels.all():
            print 'label:',i.label

    return render_to_response('articlelist.html',{'arts':arts})