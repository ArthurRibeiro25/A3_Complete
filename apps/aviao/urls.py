from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'aviao'

router = routers.DefaultRouter()
router.register('avioes', views.AvioesClassViewSet, basename='avioes')

urlpatterns = [
    path('', include(router.urls) )
]