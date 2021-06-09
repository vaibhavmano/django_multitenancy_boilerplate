from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from multi_tenancy.models.admin_models import TenantUser, Tenant


class TenantUserInline(admin.StackedInline):
    model = TenantUser
    can_delete = False
    verbose_name_plural = 'tenant_user'


class UserAdmin(BaseUserAdmin):
    inlines = (TenantUserInline,)


class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tenant, TenantAdmin)