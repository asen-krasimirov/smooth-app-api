from django.contrib.auth import get_user_model
from rest_framework import serializers
from smooth_api.main.models import Job

UserModel = get_user_model()


class SmoothUserSerializer(serializers.ModelSerializer):
    jobs = serializers.PrimaryKeyRelatedField(many=True, queryset=Job.objects.all())

    class Meta:
        model = UserModel
        fields = ['pk', 'email', 'is_business', 'jobs']
