from django.urls import path
from .views import ProfileView,ProfileEditView,AddFollower,PublicUserInfo

urlpatterns = [
    path('',ProfileView.as_view(),name='view_profile'),
    path('edit_profile/',ProfileEditView.as_view(),name='edit_profile'),
    path('add-follower/',AddFollower.as_view(),name='add-follower'),
    path('public-info/<int:pk>',PublicUserInfo.as_view(),name='public_user_info'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]
