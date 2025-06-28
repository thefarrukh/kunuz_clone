from django.urls import path
from accounts.api_endpoints.LoginSession import SessionLoginAPIView
from accounts.api_endpoints.LogoutSession import SessionLogoutAPIView

urlpatterns = [
    path('login/', SessionLoginAPIView.as_view(), name='session-login'),
    path('logout/', SessionLogoutAPIView.as_view(), name='session-logout'),
]
