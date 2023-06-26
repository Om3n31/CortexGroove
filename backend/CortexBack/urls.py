"""
URL configuration for CortexBack project.

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
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import HDF5ViewSet, NeuralNetworkViewSet, LayerViewSet, NeuralNetworkConfigViewSet, CortexViewSet, WorkspaceViewSet

router = DefaultRouter()
router.register(r'hdf5', HDF5ViewSet)
router.register(r'neuralnetwork', NeuralNetworkViewSet)
router.register(r'layer', LayerViewSet)
router.register(r'neuralnetworkconfig', NeuralNetworkConfigViewSet)
router.register(r'cortex', CortexViewSet)
router.register(r'workspace', WorkspaceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('', include(router.urls)),
]