from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^books/$',views.BooksAPIVIew.as_view()), # 保存和获取所有图书
    url(r'^book/(?P<pk>\d+)/$',views.BookAPIView.as_view()),# 单一图书的操作


]
