from django.contrib import admin

from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('smooth_api.smooth_auth.urls')),
    path('jobs/', include('smooth_api.main.urls')),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += [
    path('smooth-api-auth/', include('rest_framework.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
