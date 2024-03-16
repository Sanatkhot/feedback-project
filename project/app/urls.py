from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.AboutUs,name='aboutus'),
    path('contact',views.ContactUs,name='contactus'),
    path('course',views.course,name='course'),
    path('feedback',views.feedback,name='feedback'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout', views.signout, name='signout'),
    path('show',views.showfeed,name='showfeed'),
]
