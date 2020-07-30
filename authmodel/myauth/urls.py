from django.conf.urls import url , include
from rest_framework.routers import DefaultRouter
from .views import myBaseUserView

r = DefaultRouter()
r.register('user' , myBaseUserView)

urlpatterns = [
   # url("" , include('django.contrib.auth.urls')),
   # url('api/' , include('rest_framework.urls')),
   # url('' , include(r.urls)),
   url('rest/' , include('rest_auth.urls')) ,
   url('rest/signup' , include('rest_auth.registration.urls')),
   url('account/' , include('allauth.urls'))
]
