from django.utils import timezone
from Newcredit.Mycreditcard.models import *
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseRedirect
import json
import random

def chooseRandomID(x=random.randrange(10000,99999)):
    info = accountDatas.objects.filter(userid=x)
    if not info:
        return x
    else:
        return chooseRandomID()

# Create your views here.
def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

def online(request):
    datas = Messages.objects.order_by('-publish_date')
    return render_to_response('messageBox/online.html', {'datas':datas})

def create(request):
    return render(request, 'messageBox/create.html')

@csrf_exempt
def save(request):
    username = request.POST.get('username','')
    title = request.POST.get('title','')
    content = request.POST.get('content','')
    if username and title and content:
        Messages(username=username,title=title,content=content,publish_date=timezone.now()).save()
        return HttpResponseRedirect('/online/')
    else:
        content = {'username':username,'title':title,'content':content,'error':'error :输入信息不能为空'}
        return render_to_response('messageBox/create.html', content)

@csrf_exempt
def Delete(request,messageid):
    Messages.objects.filter(id=messageid).delete()
    return HttpResponseRedirect('/online/')

# def ZSYH(request):
#     datas = ZSYH_apply.objects.all()
#     return render_to_response('card_info.html',{'datas':datas})

def login(request):
    return render(request,'loginSys/login.html',)

# def index(request,username):
#     user_list = superuser.objects.filter(username=username)
#     context = {"user_list":user_list}
#     return render_to_response('loginSys/index.html',context)


#登录验证
@csrf_exempt
def loginVerify(request):
    errorMessage = {}
    username = request.POST['username']
    password = request.POST['password']
    info = accountDatas.objects.filter(username=username)
    if not info:
        content = {'username':username,'password':password,'error':'error :用户名不存在'}
        errorMessage['code'] = 0
        return HttpResponse(json.dumps(errorMessage), content_type="application/json")
    else:
        info = info[0]
        if info.password == password:
            request.session['member_id'] = info._id
            errorMessage['code'] = 1
            errorMessage['id']=info._id
            errorMessage['username']=username
            errorMessage['selfIntroduce'] = info.selfIntroduce
            errorMessage['phoneNumber'] = info.phoneNumber
            errorMessage['EmailAccount'] = info.EmailAccount
            errorMessage['wechatAccount'] = info.wechatAccount
            errorMessage['create_date'] = info.create_date
            errorMessage['scores'] = info.scores
            errorMessage['qqAccount']=info.qqAccount
            return HttpResponse(json.dumps(errorMessage,default=date_handler),content_type="application/json")
        else:
            errorMessage['code'] = 0
            return HttpResponse(json.dumps(errorMessage), content_type="application/json")

#加密密码
# @csrf_exempt
# def Make_password(request,passwordinput):
#     return make_password(password=passwordinput)

#登出
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

#注册页面
def regist(request):
    return render(request,'loginSys/regist.html')

#提交注册
@csrf_exempt
def registSave(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneNumber = request.POST['phonenumber']
    qqNumber = request.POST['qqnumber']
    m = accountDatas.objects.filter(username=username)
    errorMessage = {}
    if not m:
        accountDatas.objects.create(userid=chooseRandomID(),username=username,password=password,create_date=timezone.now())
        errorMessage['code']=1
        if phoneNumber:
            accountDatas.objects.filter(username=username).update(phoneNumber=phoneNumber)
        if qqNumber:
            accountDatas.objects.filter(username=username).update(qqAccount=qqNumber)
        return HttpResponse(json.dumps(errorMessage), content_type="application/json")
    else:
        content = {'username':username,'password':password,'error':'error :用户名已经存在'}
        return render(request,'loginSys/regist.html', content)

# @csrf_exempt
# def uploadImg(request):
#     if request.method == 'POST':
#         new_img = IMG(
#             img=request.FILES.get('img'),
#             name = request.FILES.get('img').name
#         )
#         new_img.save()
#     return render(request, 'img_tem/uploadimg.html')