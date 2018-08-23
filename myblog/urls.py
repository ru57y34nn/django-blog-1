from django.conf.urls import url
from django.urls import path
from .views import detail_view, list_view  # BlogIndex
from . import views

urlpatterns = [
    path('', list_view, name='blog_index'),
#    path('', BlogIndex.as_view(), name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
