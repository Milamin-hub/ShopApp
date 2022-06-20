from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.urls import re_path
from shop.views import *



urlpatterns = [
    re_path(r'^category/(?P<slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'
    ),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail'),

    re_path(r'^login/$', LoginView.as_view(
        template_name='account/login.html'), 
        name="login"
    ),
    
    re_path(r'^logout/$', LogoutView.as_view(
        template_name='account/logout.html'
        ), name="logout"
    ),
    re_path(r'^logout-then-login/$',
        logout_then_login,
        name='logout_then_login'
    ),

    re_path(r'^$', product_list, name='home'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^$', dashboard, name='dashboard'),
    re_path(r'^about/', about, name="about"),
]