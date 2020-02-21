from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from book.models import BookInfo
from book.serializers import BookInfoSerializer


def index(request):
    return HttpResponse('这里是子应用book的index_page')


class BookInfoViewSet(ModelViewSet):
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()
