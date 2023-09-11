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
from django.apps import apps
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter
from rest_framework import serializers, viewsets
from . import models
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import action
from rest_framework.response import Response
from functools import partial

router = DefaultRouter()


def handle_custom_action(self, request, pk=None, model=None, action_func=None):
    # get the model instance based on pk
    instance = model.objects.get(pk=pk)
    # call the action function
    result = action_func(instance)
    return Response({'result': result})

def dynamic_view(request, model_name, action_name):
    """Dynamically create a view for the given model and action."""
    model = getattr(models, model_name)
    action = getattr(model, action_name)

    return action(request)

for model in apps.get_models():
    model_name = model.__name__
    serializer = type(
        f'{model_name}Serializer', 
        (serializers.ModelSerializer,), 
        {'Meta': type('Meta', (object,), {'model': model, 'fields': '__all__'})}
    )

    # Get the allowed methods from the model
    allowed_methods = getattr(model, 'allowed_methods', ['get', 'post', 'head', 'options', 'put', 'patch', 'delete'])

    viewset = type(
        f'{model_name}ViewSet',
        (viewsets.ModelViewSet,),
        {'queryset': model.objects.all(), 'serializer_class': serializer, 'http_method_names': allowed_methods}
    )

    for attr in dir(model):
        func = getattr(model, attr)
        if hasattr(func, 'api_action'):
            
            action_decorator = action(detail=True, methods=[func.api_action['method']])
            decorated_func = action_decorator(func)

            # setattr(viewset, func.api_action['name'], test)
            setattr(viewset, func.api_action['name'], decorated_func)
            # viewset.do_action("test")

    router.register(rf'{model_name.lower()}', viewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('', include(router.urls)),
]