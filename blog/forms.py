# coding=utf-8
from django import forms
from django.forms import widgets
from models import Article,Label
from django.contrib.auth.models import User

class NewArticleForm(forms.Form):
    title = forms.CharField(max_length=10,required=True,error_messages={'required': u'必选项1'})
    content = forms.CharField(max_length=3000,error_messages={'required': u'必选项2'})
    label= forms.IntegerField(required=False,error_messages={'required': u'必选项3'})
#    lebel2 = forms.ChoiceField(label='标签2：',required=False)
    def save(self):
        newarticle=Article(title=self.cleaned_data['title'],
                           content=self.cleaned_data['content'])
        newarticle.save()
        print self.cleaned_data['label']
        labs=self.cleaned_data['label']
        if labs:
            newarticle.labels.add(labs)
        else:
            newarticle.labels.add('1')
            print 'label add error'
        return newarticle

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4,max_length=12, required=True, error_messages={'required': u'用户名不能为空'})
    password = forms.CharField(min_length=4,max_length=12, required=True, error_messages={'required': u'密码不能为空'})

    def clean(self):
        #用户名
        try:
            username = self.cleaned_data['username']
        except Exception as e:
            print 'except:'+str(e)
            raise forms.ValidationError(u'用户名有误')

        #密码
        try:
            password = self.cleaned_data['password']
        except Exception as e:
            print 'except:'+str(e)
            raise forms.ValidationError(u'密码有误')

        #验证用户名存在
        is_username_exist = User.objects.filter(username=username).exists()
        if not is_username_exist:
            raise forms.ValidationError(u'该账号不存在')

        #验证用户名、密码
        is_user = User.objects.filter(username=username,password=password).exists()
        if not is_user:
            raise forms.ValidationError(u'用户名、密码有误')