from typing import Any
from django.db import models
from main_lib.iNeuralNetwork import INeuralNetwork, Position
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.db.models.signals import post_save
from django.dispatch import receiver

class HDF5(models.Model):
    data = models.BinaryField()  # Binaries
    state = models.TextField()
    allowed_methods = ['get']

class NeuralNetwork(models.Model):
    hdf5 = models.ForeignKey(HDF5, on_delete=models.CASCADE)
    input_shape = models.JSONField()  # int table

class Cortex(models.Model):
    metadata = models.TextField()  # string
    
class NeuralNetworkConfig(models.Model):
    neural_network = models.OneToOneField(NeuralNetwork, null=True, on_delete=models.CASCADE)  # N:1
    next_NN = models.ManyToManyField('self', blank=True)  # N:N
    previous_NN = models.ManyToManyField('self', blank=True)  # N:N
    cortex = models.ForeignKey(Cortex, default=None, on_delete=models.CASCADE)
    position = models.IntegerField(default=1, choices=Position.format())

    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super().__init__(*args, **kwargs)


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

