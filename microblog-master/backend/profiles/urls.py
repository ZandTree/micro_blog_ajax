from django.urls import path
from .views import ProfileView,ProfileEditView,AddFollower

urlpatterns = [
    path('',ProfileView.as_view(),name='view_profile'),
    path('edit_profile/',ProfileEditView.as_view(),name='edit_profile'),
    path('add-follower/',AddFollower.as_view(),name='add-follower'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]
