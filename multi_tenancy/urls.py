from django.contrib import admin
from django.urls import path, include

from multi_tenancy.views import CustomTokenView, CustomRevokeTokenView

urlpatterns = [
    path('token', CustomTokenView.as_view(), name='custom_token'),
    path(
        'revoke-token', CustomRevokeTokenView.as_view(),
        name='custom_revoke_token'
    ),
]
