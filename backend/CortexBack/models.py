from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Layer

class HDF5(models.Model):
    data = models.BinaryField()  # Binaries
    state = models.TextField()
    allowed_methods = ['get']

class NeuralNetwork(models.Model):
    hdf5 = models.ForeignKey(HDF5, on_delete=models.CASCADE)
    input_shape = models.JSONField()  # int table

class Layer(models.Model):
    index = models.IntegerField()

class NeuralNetworkConfig(models.Model):
    neural_network = models.OneToOneField(NeuralNetwork, on_delete=models.CASCADE)  # N:1
    post_nn = models.ManyToManyField(NeuralNetwork, related_name='post_nn_configs')  # N:N
    pre_nn = models.ManyToManyField(NeuralNetwork, related_name='pre_nn_configs')  # N:N
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)

class Cortex(models.Model):
    metadata = models.TextField()  # string
    layers = models.ManyToManyField(Layer)  # List of Layer

class TFLayerTypeOption(models.Model):
    name = models.TextField()
    type = models.TextField()
    possible_values = models.JSONField()

class TFLayerType(models.Model):
    name = models.TextField() 
    options = models.ManyToManyField(TFLayerTypeOption, blank=True) 
    
# @functools.wraps
def api_action(name, method):
    def wrapper(func):
        func.api_action = {
            'name': name,
            'method': method
        }
        return func
    return wrapper

class Workspace(models.Model):
    cortex = models.OneToOneField(Cortex, on_delete=models.CASCADE)

    @api_action('do_action', 'POST')
    def do_action(self, request, pk=None):
        print("test")
        # workspace = Workspace.objects.first() # Change this line to get the correct Workspace instance
        # workspace.doAction()
        return Response({"status": "success"}, status=status.HTTP_200_OK)


@receiver(post_save, sender=Layer)
def new_layer_handler(sender, instance, created, **kwargs):
    if created:
        # Trigger logic here
        print(f"New layer added: {instance.index}")