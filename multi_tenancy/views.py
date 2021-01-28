from django.http import HttpResponse
from oauth2_provider.views.base import TokenView, RevokeTokenView
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
import json
import os
import sys
import logging

from multi_tenancy.wrapper import CustomResponse


class CustomTokenView(TokenView):
    """
    A Custom Token View that is an extension of the
    TokenView class in django-oauth-toolkit
    """
    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            body = json.loads(body)
            access_token = body.get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(
                    token=access_token)
                app_authorized.send(
                    sender=self, request=request,
                    token=token)
                body = CustomResponse.build_response(True, body)
                body = json.dumps(body)
        else:
            body = json.loads(body)
            body = CustomResponse.build_response(False, [body['error']])
            body = json.dumps(body)

        response = HttpResponse(content=body, status=status)
        for k, v in headers.items():
            response[k] = v
        return response


class CustomRevokeTokenView(RevokeTokenView):
    """
    A Custom Revoke Token View that is an extension of the
    TokenView class in django-oauth-toolkit
    """
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_revocation_response(request)
        if status == 200:
            headers = {
                'Content-Type': 'application/json',
                'Cache-Control': 'no-store',
                'Pragma': 'no-cache',
                'WWW-Authenticate': 'Bearer, error="invalid_client"'
            }
            body = CustomResponse.build_response(True, body)
            body = json.dumps(body)
        else:
            body = json.loads(body)
            body = CustomResponse.build_response(False, [body['error']])
            body = json.dumps(body)

        response = HttpResponse(content=body or "", status=status)

        for k, v in headers.items():
            response[k] = v
        return response
