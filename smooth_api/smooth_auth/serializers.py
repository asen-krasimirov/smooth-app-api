from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from smooth_api.smooth_auth.models import BusinessProfile, ApplicantProfile

UserModel = get_user_model()


class SmoothUserSerializer(serializers.ModelSerializer):

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
        is_business = validated_data['is_business']

        user = UserModel.objects.filter(email=email).first()
        if not user:
            new_user = UserModel.objects.create(
                email=email,
                password=password,
                is_business=is_business,
            )

            return new_user
        raise ValidationError({'error_message': 'User with this email already exists!'})


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
        raise ValidationError({'error_message': 'Wrong credentials!'})


class BusinessProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = BusinessProfile
        fields = [
            'id',
            'name',
            'sub_name',
            'about_info',
            'icon_image',
            'background_image',
            'business_website',
            # 'is_complete'
        ]

    def update(self, instance, validated_data):

        name = validated_data['name']
        sub_name = validated_data['sub_name']
        about_info = validated_data['about_info']
        icon_image = validated_data['icon_image']
        background_image = validated_data['background_image']
        business_website = validated_data['business_website']

        instance.name = name
        instance.sub_name = sub_name
        instance.about_info = about_info
        instance.icon_image = icon_image
        instance.background_image = background_image
        instance.business_website = business_website

        instance.save()
        return instance


class ApplicantProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.pk')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = ApplicantProfile
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'about_info',
            'icon_image',
            'background_image',
            'skills',
            'education',
            'applicant_blog',
            'phone_number',
            'preferred_position',
            # 'is_complete'
        ]

    def update(self, instance, validated_data):

        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        about_info = validated_data['about_info']
        icon_image = validated_data['icon_image']
        background_image = validated_data['background_image']
        skills = validated_data['skills']
        education = validated_data['education']
        applicant_blog = validated_data['applicant_blog']
        phone_number = validated_data['phone_number']
        preferred_position = validated_data['preferred_position']

        instance.first_name = first_name
        instance.last_name = last_name
        instance.about_info = about_info
        instance.icon_image = icon_image
        instance.background_image = background_image
        instance.skills = skills
        instance.education = education
        instance.applicant_blog = applicant_blog
        instance.phone_number = phone_number
        instance.preferred_position = preferred_position

        instance.save()
        return instance
