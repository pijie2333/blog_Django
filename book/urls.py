from . import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^index/$',views.index),


]
router = DefaultRouter()
router.register(r'book',views.BookInfoViewSet)
urlpatterns += router.urls
