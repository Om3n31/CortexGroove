

from CortexBack.controller.CortexManager import CortexManager
from CortexBack.models import NeuralNetworkConfig
from django.dispatch import receiver

from django.db.models.signals import post_save
from main_lib.iNeuralNetwork import INeuralNetwork, Position

@receiver(post_save, sender=NeuralNetworkConfig)
def new_neuralNetworkConfig_handler(sender, instance : NeuralNetworkConfig, created, **kwargs):
    if created:
        # Trigger logic here

        

        print(f"New NeuralNetworkConfig added: {instance.index}")