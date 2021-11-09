from django.urls import path
from smooth_api.smooth_auth import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', views.SmoothUserViewSet)
# urlpatterns = router.urls


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
