from django.urls import path

from userpreferences.views.custom_user_views import (
    CustomUserCreateView, CustomUserListView, CustomUserUpdateView, CustomUserDeleteView,
)

from userpreferences.views.sectors_views import (
    SectorsCreateView, SectorsListView, SectorsUpdateView, SectorsDeleteView
)

urlpatterns = [
    path('create-custom-user/', CustomUserCreateView.as_view(), name='create-user'),
    path('list-custom-users/', CustomUserListView.as_view(), name='list-users'),
    path('update-custom-user/<int:user_id>/', CustomUserUpdateView.as_view(), name='update-user'),
    path('delete-custom-user/<int:user_id>/', CustomUserDeleteView.as_view(), name='delete-user'),
    path('create-sector/', SectorsCreateView.as_view(), name='create-sector'),
    path('list-sectors/', SectorsListView.as_view(), name='list-sectors'),
    path('update-sector/<int:sector_id>/', SectorsUpdateView.as_view(), name='update-sector'),
    path('delete-sector/<int:user_id>/', SectorsDeleteView.as_view(), name='delete-sector'),
]