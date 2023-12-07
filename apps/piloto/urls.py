from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'piloto'

router = routers.DefaultRouter()
router.register('pilotos', views.PilotosClassViewSet, basename='pilotos')

urlpatterns = [
    path('', include(router.urls) )
]