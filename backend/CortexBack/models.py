from typing import Any
from CortexBack.controller.CortexManager import CortexManager
from CortexBack.utils.SingletonMeta import api_action
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

    @api_action('predict', 'POST')
    def predict(self, request, pk=None):
        print(request.data)
        CortexManager().neural_net_matrix = list(NeuralNetworkConfig.objects.all())
        data = CortexManager().start(request.data)
        print("prediction")
        # workspace = Workspace.objects.first() # Change this line to get the correct Workspace instance
        # workspace.doAction()
        return Response({"status": "success", "data" : str(data)}, status=status.HTTP_200_OK)
    
class NeuralNetworkConfig(models.Model, INeuralNetwork):
    neural_network = models.OneToOneField(NeuralNetwork, null=True, on_delete=models.CASCADE)  # N:1
    next_NN = models.ManyToManyField('self', blank=True)  # N:N
    previous_NN = models.ManyToManyField('self', blank=True)  # N:N
    cortex = models.ForeignKey(Cortex, default=None, on_delete=models.CASCADE)
    position = models.IntegerField(default=1, choices=Position.format())

    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super().__init__(*args, **kwargs)
    
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__init__ = lambda self: None

class TFLayerTypeOption(models.Model):
    name = models.TextField()
    type = models.TextField()
    possible_values = models.JSONField()

class TFLayerType(models.Model):
    name = models.TextField() 
    options = models.ManyToManyField(TFLayerTypeOption, blank=True) 
    

class Workspace(models.Model):
    cortex = models.OneToOneField(Cortex, on_delete=models.CASCADE)

    @api_action('do_action', 'POST')
    def do_action(self, request, pk=None):
        print("test")
        # workspace = Workspace.objects.first() # Change this line to get the correct Workspace instance
        # workspace.doAction()
        return Response({"status": "success"}, status=status.HTTP_200_OK)

