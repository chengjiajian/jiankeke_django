from django.conf.urls import url
from Newcredit.Mycreditcard.views import *

urlpatterns = [
    url(r'create',create,name='create'),
    url(r'^save/',save,name='save'),
    url(r'^delete/(?P<messageid>\d+)/$',Delete,name='delete'),
    url(r'^$', login, name='login'),
    url(r'^loginVerify/$', loginVerify, name='loginVerify'),
    url(r'^registSave/$',registSave,name='registSave'),
    url(r'^regist/$',regist,name='regist'),
    #url(r'^index/$', index, name='index'),
]