from rest_framework import serializers
from smooth_api.main.models import Job


class JobSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner.pk')

    class Meta:
        model = Job
        fields = ['id', 'owner_id', 'title', 'description', 'type', 'status']
