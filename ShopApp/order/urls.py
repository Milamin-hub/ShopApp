from django.urls import re_path
from order.views import *


urlpatterns = [
    re_path(r'^create/$', order_create, name='order_create'),
]