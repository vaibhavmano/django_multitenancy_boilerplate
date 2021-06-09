from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from django_boilerplate.config import DjangoConfig
from multi_tenancy.wrapper import CustomResponse


class SetTenantId:

    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        try:
            if request.path.startswith("/admin"):
                return self.get_response(request)
            if request.path.startswith("/auth") and (
                    not request.path.startswith("/auth/change-password")):
                return self.get_response(request)

            if DjangoConfig.ENVIRONMENT == "DEBUG":
                username = request.headers['Authorization']
                SetTenantId.set_tenant_id(request, username)

            if DjangoConfig.ENVIRONMENT == "PRODUCTION":
                username = request.user
                if request.user.is_authenticated:
                    SetTenantId.set_tenant_id(request, username)
                else:
                    raise PermissionDenied
            response = self.get_response(request)
            return response
        except (User.DoesNotExist, PermissionDenied) as e:
            data = CustomResponse.build_response(False, ['User not found'])
            response = JsonResponse(data, status=status.HTTP_401_UNAUTHORIZED)
            return response

        except Exception as e:
            data = CustomResponse.build_response(False, [str(e)])
            response = JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
            return response

    @staticmethod
    def set_tenant_id(request, username):
        user = User.objects.get(username=username)
        request.session['current_tenant_id'] = user.tenantuser.tenant.id.__str__()
        request.session['current_user_id'] = user.id.__str__()
        request.session['role'] = user.tenantuser.role
