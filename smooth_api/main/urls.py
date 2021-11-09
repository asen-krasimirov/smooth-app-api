# from smooth_api.smooth_auth import views
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'jobs', views.job_list)
# urlpatterns = router.urls

from django.urls import path
from smooth_api.main import views


urlpatterns = [
    path('', views.JobList.as_view()),
    path('<int:pk>/', views.JobDetail.as_view()),
]
