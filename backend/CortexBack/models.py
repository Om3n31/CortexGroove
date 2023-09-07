from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

    @api_action('action_name', 'POST')
    def do_action(self, request):
        print("test")
        # workspace = Workspace.objects.first() # Change this line to get the correct Workspace instance
        # workspace.doAction()
        # return Response({"status": "success"}, status=status.HTTP_200_OK)