from django.urls import path, include
from django.conf.urls import url

from ShoppersPoint import views

urlpatterns = [
    #url(r'^$', views.home_page, name='home'),
    path('', views.home_page, name='home'),
    path('user/', include('user.urls', namespace ='user')),
    path('search/<str:search_query>', views.search, name='search'),
    url(r'^(?P<category>[-\w]+)/$', views.category_view, name='category'),
    url(r'^product/(?P<product_id>[-\w]+)/$', views.product_page, name='product_page'),
    #url(r'^search/$', views.search, name='search'),

]