from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Testproject.models import TestProject, TestEnv, TestFile
from .serializer import TestProjectSerializer, TestEnvSerializer, TestFileSerializer
from rest_framework import permissions
# Create your views here.

class TestProjectView(ModelViewSet):
    queryset = TestProject.objects.all()
    serializer_class = TestProjectSerializer
    # 添加视图的权限校验（需要登录才能访问，访问的时候需要在请求头中添加token）
    permission_classes = [permissions.IsAuthenticated]

# 测试环境管理的接口开发（增删查改）
class TestEnvView(ModelViewSet):
    queryset = TestEnv.objects.all()
    serializer_class = TestEnvSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']
