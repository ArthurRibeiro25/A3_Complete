from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'passageiro'

router = routers.DefaultRouter()
router.register('passageiros', views.PassageirosClassViewSet, basename='passageiros')

urlpatterns = [
    path('', include(router.urls) )
]