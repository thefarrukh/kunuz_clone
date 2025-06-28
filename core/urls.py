from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from accounts.api_endpoints.Profile.Register.views import ConfirmEmailAPIView
from accounts.api_endpoints.Profile.Register.views import RegisterUserAPIView, ConfirmEmailAPIView
from accounts.api_endpoints.Profile.PasswordReset.views import PasswordResetRequestAPIView, PasswordResetConfirmAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,   
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="KunUz Clone API",
      default_version='v1',
      description="Test API for news and comments",
      contact=openapi.Contact(email="farrux@example.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', include('news.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/accounts/', include('accounts.urls')),  
    path('i18n/', include('django.conf.urls.i18n')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-email/', ConfirmEmailAPIView.as_view(), name='verify-email'),

    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('verify-email/', ConfirmEmailAPIView.as_view(), name='verify-email'),
    path('password-reset/delete/', PasswordResetRequestAPIView.as_view(), name='passwordreset-delete'),
    path('password-reset/update/', PasswordResetConfirmAPIView.as_view(), name='passwordreset-update'),

    path('rosetta/', include('rosetta.urls')),

    # Swagger va Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
