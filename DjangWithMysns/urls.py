"""DjangWithMysns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from my_sns.api.user import User

# swagger 관련 모듈 import
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# swagger에 적는 프로젝트의 전반적인 정보를 기재
schema_view = get_schema_view(
    openapi.Info(
        title='장고 테스트 - MySNS',
        default_version='v1',
        description='장고를 이용해서 생성했음'
    ),
    public=True,
    permission_classes=(AllowAny)   
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', User.as_view(), name='user'),
]

