from importlib._common import _

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# from carrent.carrent_auth.models import CarRentUser, CarRentProfile
from smooth_api.smooth_auth.models import SmoothUser, BusinessProfile, ApplicantProfile, SmoothSession

UserModel = get_user_model()


@admin.register(SmoothUser)
class SmoothUserAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {
            'fields': ('is_business', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'is_staff', 'is_business')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(SmoothSession)
class SmoothSessionAdmin(admin.ModelAdmin):
    pass
