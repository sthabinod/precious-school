from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from .views import MyObtainTokenPairView

urlpatterns = [
    path('',views.AuthenticationUser.as_view(),name='welcome'),
    path('invite-user',views.CreateUser.as_view(),name='invite-user'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset-request',views.TokenGeneratorEmailView.as_view(),name="request-reset-email"),
    path('password-change/<uidb64>/<token>/',views.PasswordTokenCheckAPI.as_view(),name="password-change" ),
    path('password-reset-complete',views.SetNewPasswordView.as_view(),name="password-change-complete"),
    # path('invite-user',views.)
]