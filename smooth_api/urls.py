from django.contrib import admin
# from django.urls import path, include

from django.urls import include, path
# from rest_framework import routers
# from tutorial.quickstart import views
# from smooth_api.smooth_auth import views


# router = routers.DefaultRouter()
# router.register(r'users', views.SmoothUserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('smooth_api.smooth_auth.urls')),
    path('jobs/', include('smooth_api.main.urls')),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += [
    path('smooth-api-auth/', include('rest_framework.urls')),
]