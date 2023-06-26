from rest_framework import serializers
from .models import HDF5, NeuralNetwork, Layer, NeuralNetworkConfig, Cortex, Workspace


class HDF5Serializer(serializers.ModelSerializer):
    class Meta:
        model = HDF5
        fields = '__all__'


class NeuralNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeuralNetwork
        fields = '__all__'


class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'


class NeuralNetworkConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeuralNetworkConfig
        fields = '__all__'


class CortexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cortex
        fields = '__all__'


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'
