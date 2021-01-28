from rest_framework.response import Response
from rest_framework import status


class CustomResponse:
    """
    It is a custom response wrapper function.
    Import and use throughout the application
    """
    def __init__(self):
        pass

    @staticmethod
    def custom_response(success_status: bool, data):
        data = CustomResponse.build_response(success_status, data)
        if success_status is True:
            return Response(data, status=status.HTTP_200_OK)
        elif success_status is False:
            return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def build_response(success_status, data):
        new_data = {}
        if success_status is True:
            new_data['data'] = data
            new_data['success'] = success_status
        elif success_status is False:
            new_data['data'] = list()
            new_data['errors'] = data
            new_data['success'] = success_status
        return new_data
