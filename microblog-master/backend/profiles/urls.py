from django.urls import path
from .views import ProfileView,ProfileEditView

urlpatterns = [
    path('',ProfileView.as_view(),name='view_profile'),
    path('edit_profile/',ProfileEditView.as_view(),name='edit_profile'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]
