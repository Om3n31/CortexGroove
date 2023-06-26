from rest_framework import viewsets
from .models import HDF5, NeuralNetwork, Layer, NeuralNetworkConfig, Cortex, Workspace
from .serializers import HDF5Serializer, NeuralNetworkSerializer, LayerSerializer, NeuralNetworkConfigSerializer, CortexSerializer, WorkspaceSerializer


class HDF5ViewSet(viewsets.ModelViewSet):
    queryset = HDF5.objects.all()
    serializer_class = HDF5Serializer


class NeuralNetworkViewSet(viewsets.ModelViewSet):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer


class LayerViewSet(viewsets.ModelViewSet):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer


class NeuralNetworkConfigViewSet(viewsets.ModelViewSet):
    queryset = NeuralNetworkConfig.objects.all()
    serializer_class = NeuralNetworkConfigSerializer


class CortexViewSet(viewsets.ModelViewSet):
    queryset = Cortex.objects.all()
    serializer_class = CortexSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
