from django.urls import re_path
from shop.views import *


urlpatterns = [
    re_path(r'^$', product_list, name='home'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail'),
]