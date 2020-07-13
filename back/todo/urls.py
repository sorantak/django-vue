from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views.todo import *  # views/__init__.py 에서 status_check.py를 모듈로 선언했기에 한번에 가져올 수 있습니다.
from todo.views.status_check import *

router = DefaultRouter()  # viewset 은 router 를 사용하여 URL 을 관리할 수 있습니다.
router.register(r'todo', TodoModelViewSet)


urlpatterns = [
    # endpoints
    path('status_check/', status_check, name='status_check'),  # /api/status_check/
    path('', include(router.urls))
]