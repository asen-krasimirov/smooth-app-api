from django.urls import path
from smooth_api.main import views


urlpatterns = [
    path('', views.JobList.as_view()),
    path('<int:pk>/', views.JobDetail.as_view()),
    # path('test/', views.test_view),
    path('applied/', views.AppliedJobs.as_view()),
]
