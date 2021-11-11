from django.urls import path

from knox import views as knox_views

from smooth_api.smooth_auth import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', views.SmoothUserViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # path('login/', views.LoginView.as_view()),
    # path('logout/', knox_views.LogoutView.as_view()),
]
