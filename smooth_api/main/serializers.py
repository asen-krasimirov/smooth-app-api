# # from django.contrib.auth.models import User, Group
# # from rest_framework import serializers
#
#
# # from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# from models import Job, JOB_TYPE_CHOICES, HIRING_STATUS_CHOICES
# from rest_framework import serializers
#
#
# class JobSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#
#     # owner = serializers.ForeignKey(
#     #     UserModel,
#     #     on_delete=models.CASCADE,
#     # )
#
#     title = serializers.CharField(
#         max_length=100,
#     )
#
#     description = serializers.CharField(
#         max_length=2500,
#     )
#
#     type = serializers.ChoiceField(
#         choices=JOB_TYPE_CHOICES,
#     )
#
#     status = serializers.ChoiceField(
#         choices=HIRING_STATUS_CHOICES,
#     )
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Job` instance, given the validated data.
#         """
#
#         return Job.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.type = validated_data.get('type', instance.type)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance

from rest_framework import serializers
from smooth_api.main.models import Job


class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Job
        fields = ['pk', 'owner', 'title', 'description', 'type', 'status']
