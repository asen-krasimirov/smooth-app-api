from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

from smooth_api.main.models import Job
from smooth_api.smooth_auth.models import SmoothSession

UserModel = get_user_model()


class SmoothUserSerializer(serializers.ModelSerializer):

    # jobs = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Job.objects.all(),
    # )

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'is_business']

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
    )

    is_business = serializers.BooleanField(
        default=False,
    )

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        user = UserModel.objects.filter(email=email).first()
        if not user:
            new_user = UserModel.objects.create(
                email=email,
                password=password,
            )

            return new_user
        raise ValidationError('User with this email already exists!')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
    )

    def validate(self, data):
        email = data['email']
        password = data['password']

        user = UserModel.objects.filter(email=email).first()

        if user and user.password == password:
            return user
        raise ValidationError('Wrong credentials!')
