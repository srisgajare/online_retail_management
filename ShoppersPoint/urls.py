from django.urls import path, include
from django.conf.urls import url

from ShoppersPoint import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('user/', include('user.urls', namespace ='user')),
    path('search/<str:search_query>', views.search, name='search'),
    path('category/<str:category>/<int:page_index>', views.category_view, name='category'),
    url(r'^product/(?P<product_id>[-\w]+)/$', views.product_page, name='product_page'),

]