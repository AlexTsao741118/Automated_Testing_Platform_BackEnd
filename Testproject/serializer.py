from .models import TestProject, TestEnv, TestFile
from rest_framework import serializers

class TestProjectSerializer(serializers.ModelSerializer):
    """测试项目的序列化器"""
    class Meta:
        model = TestProject
        fields = "__all__"

class TestEnvSerializer(serializers.ModelSerializer):
    """测试环境的序列化器"""
    class Meta:
        model = TestEnv
        fields = "__all__"

class TestFileSerializer(serializers.ModelSerializer):
    """测试文件的序列化器"""
    class Meta:
        model = TestFile
        fields = "__all__"