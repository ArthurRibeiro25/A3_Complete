from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'passagem'

router = routers.DefaultRouter()
router.register('passagens', views.PassagensClassViewSet, basename='passagens')

urlpatterns = [
    path('', include(router.urls) )
]