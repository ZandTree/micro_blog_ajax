from django.urls import path
from backend.app import views

urlpatterns = [
    path('', views.AllPost.as_view(), name="posts"),
    path('myfans/',views.MyFansPostList.as_view(),name='myfans'),
    path('like/', views.Like.as_view(),name='like'),
    path('favorites/',views.PostsIFollow.as_view(),name='favorites'),

]
