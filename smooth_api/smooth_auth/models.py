import datetime

from cloudinary import models as cloudinary_models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.db import models


class SmoothUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, password, **extra_fields)


class SmoothUser(AbstractBaseUser, PermissionsMixin):
    """
    User model that extends the default one.
    Now the UserModel (user) has to log-in with email and password.
    """

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_business = models.BooleanField(
        default=False
    )

    # jobs = models.ForeignKey()
    jobs = None

    USERNAME_FIELD = 'email'

    objects = SmoothUserManager()

    class Meta:
        db_table = 'smoothuser'
        verbose_name = 'Smooth User'


class BusinessProfile(models.Model):
    """
    This is the profile businesses will use.
    """

    name = models.CharField(
        max_length=60,
    )

    sub_name = models.CharField(
        max_length=100,
    )

    about_info = models.CharField(
        max_length=300,
    )

    icon_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    background_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    business_website = models.URLField(
        blank=True,
    )

    user = models.OneToOneField(
        SmoothUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    is_complete = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'Profile of {self.user.email}'

    class Meta:
        verbose_name = 'Business Profile'


class ApplicantProfile(models.Model):
    """
    This is the profile job applicants will use.
    """

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    about_info = models.CharField(
        max_length=300,
    )

    icon_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    background_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    skills = ArrayField(
        models.CharField(
            max_length=100,
        ),
        blank=True,
    )

    education = ArrayField(
        models.CharField(
            max_length=150,
        ),
        blank=True,
    )

    applicant_blog = models.URLField(
        blank=True,
    )

    user = models.OneToOneField(
        SmoothUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    is_complete = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'Profile of {self.user.email}'

    class Meta:
        verbose_name = 'Applicant Profile'


class SmoothSession(models.Model):
    user = models.OneToOneField(
        SmoothUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    token = models.CharField(
        max_length=64,
    )

    set_data = models.DateTimeField(
        default=datetime.datetime.now()
    )

    expiry_data = models.DateTimeField(
        default=datetime.datetime.now()
    )

    def has_expired(self):
        return datetime.datetime.now(self.expiry_data.tzinfo) > self.expiry_data
