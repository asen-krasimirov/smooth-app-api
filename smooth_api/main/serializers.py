from rest_framework import serializers
from smooth_api.main.models import Job, AppliedJob


class JobSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner.pk')

    class Meta:
        model = Job
        fields = ['id', 'owner_id', 'title', 'description', 'type', 'status']


class AppliedJobSerializer(serializers.ModelSerializer):
    job_id = serializers.ReadOnlyField(source='job.pk')
    user_id = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = AppliedJob
        fields = ['id', 'job_id', 'user_id']
