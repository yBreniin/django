from django.contrib import admin
from django.urls import path, include
from tasks.views import TasksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TasksViewSet, basename='Tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
