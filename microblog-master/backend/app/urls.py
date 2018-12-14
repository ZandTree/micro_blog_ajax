from django.urls import path
from .views import *

urlpatterns = [
    path('', AllPost.as_view(), name="posts"),
    path('like/', Like.as_view(),name='like'),
    path('mypost/',MyPostView.as_view(),name='mypost'),
    path('favorites/',PostsIfollow.as_view(),name='favorites'),

]
