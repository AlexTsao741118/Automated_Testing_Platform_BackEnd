from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class LoginView(TokenObtainPairView):
    """自定義登錄返回的數據"""

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        # 自定義登錄返回的字段
        result = serializer.validated_data
        result_data = {}
        result_data['token'] = result['access']
        result_data['refresh'] = result['refresh']

        return Response(result_data, status=status.HTTP_200_OK)
    