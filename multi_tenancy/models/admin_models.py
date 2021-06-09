from django.db import models
import uuid
from django.contrib.auth.models import User
from django_enum_choices.fields import EnumChoiceField
from django_enum_choices.choice_builders import attribute_value

from multi_tenancy.models.lookups import UserRole


class Tenant(models.Model):
    """
    The tenants are the audit firms, identified by their UUID.
    The Tenant ID is not exposed to the API response.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tenants"

    def __str__(self):
        return self.name


class TenantBaseModel(models.Model):
    """
    Abstract class which should be extended by all the tenant-specific models.
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TenantUser(TenantBaseModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = EnumChoiceField(UserRole, choice_builder=attribute_value, default=UserRole.USER)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "tenantuser"

