from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)