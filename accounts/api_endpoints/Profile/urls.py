from django.urls import path
from accounts.api_endpoints.Profile import *

urlpatterns = [
    path('profile/delete/', ProfileDeleteAPIView.as_view(), name="profile"),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name="profile-update"),

    path('password-reset/request/', PasswordResetRequestAPIView.as_view(), name="password-reset"),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
    
    path('register/', RegisterUserAPIView.as_view(), name="register"),
    path('register/confirm/', ConfirmEmailAPIView.as_view(), name="register-confirm"),
]