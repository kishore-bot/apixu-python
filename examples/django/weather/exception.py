from rest_framework import status
from rest_framework.response import Response
from apixu.client import ApixuException
import logging


def handler(exc, context):
    message = 'Internal Server Error'
    code = status.HTTP_500_INTERNAL_SERVER_ERROR

    if isinstance(exc, ApixuException):
        if exc.code == 1006:
            message = 'Could not find location.'
            code = status.HTTP_404_NOT_FOUND
        logging.exception(exc)

    if isinstance(exc, ValueError):
        message = str(exc)
        code = status.HTTP_400_BAD_REQUEST

    return Response({'error': message}, status=code)
