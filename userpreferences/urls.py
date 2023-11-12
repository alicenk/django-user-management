from django.urls import path

from userpreferences.views.custom_user_views import (
    CustomUserCreateView, CustomUserListView, CustomUserUpdateView, CustomUserDeleteView
)

urlpatterns = [
    path('create-custom-user/', CustomUserCreateView.as_view(), name='create-user'),
    path('list-custom-users/', CustomUserListView.as_view(), name='list-users'),
    path('update-custom-user/<int:user_id>/', CustomUserUpdateView.as_view(), name='update-user'),
    path('delete-custom-user/<int:user_id>/', CustomUserDeleteView.as_view(), name='delete-user'),
]