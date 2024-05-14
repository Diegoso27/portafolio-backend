from accounts.api.views import registration_view, session_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path










urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', registration_view, name='register'),
    path('session/', session_view, name='session'),
    
]
