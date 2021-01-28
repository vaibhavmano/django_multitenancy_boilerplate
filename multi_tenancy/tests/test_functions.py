from django.contrib.auth.models import User

from multi_tenancy.models.admin_models import Tenant, TenantUser


def create_user(tenant_obj, username='test@prudent.ai'):
    user = User.objects.create_user(username, username, 'abc@12345')
    tenant_user = TenantUser.objects.create(user=user, tenant_id=tenant_obj.id)
    return user, tenant_user


def create_tenant(name='Test Tenant 1'):
    tenant_obj = Tenant.objects.create(name=name)
    return tenant_obj
