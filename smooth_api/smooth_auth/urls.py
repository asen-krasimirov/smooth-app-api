from django.urls import path

from smooth_api.smooth_auth import views

import smooth_api.smooth_auth.signals


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # path('create-business-profile/<int:owner_id>/', views.BusinessProfileView.as_view()),
    path('profile-details/<int:user_id>/', views.ProfileDetails.as_view()),
]
