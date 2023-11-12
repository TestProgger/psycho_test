from rest_framework import status
from typing import Union
from rest_framework.response import Response


class ResponseMixin:

    def make_response(self,
                      code: int = status.HTTP_200_OK,
                      message: str = 'OK',
                      body: Union[dict, list, bool] = None
                      ):
        return Response(
            data={
                "body": body if body else {},
                "status": {
                    "code": code,
                    "message": message
                }
            },
            status=code
        )

    def success_response(self, body: Union[dict, list, bool] = None, message: str = None):
        return self.make_response(body=body, message=message)

    def error_response(self, message: str, code: int = status.HTTP_400_BAD_REQUEST):
        return self.make_response(code=code, message=message)