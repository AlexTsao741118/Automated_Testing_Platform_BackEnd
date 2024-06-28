"""
URL configuration for ApiTestPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 登录接口的访问路径
    # path('bryant-admin/users/login', TokenObtainPairView.as_view(), name='login'),
    path('bryant-admin/users/login', LoginView.as_view(), name='login'),
    # 刷新token
    path('bryant-admin/users/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # 校验token有效
    path('bryant-admin/users/token/verify', TokenVerifyView.as_view(), name='token_verify')
]

# 导入drf的路由和自定的视图集
from rest_framework import routers
from Testproject.views import TestProjectView, TestEnvView

# 创建一个对应对象
router = routers.SimpleRouter()
# 注册项目管理的路由
router.register('bryant-admin/testPro/projects', TestProjectView)
# 注册项目管理的路由
router.register('bryant-admin/testPro/envs', TestEnvView)

urlpatterns += router.urls
