from CortexBack.utils.SingletonMeta import SingletonMeta
from main_lib.Engine import Engine
from main_lib.iNeuralNetwork import INeuralNetwork, Position


class CortexManager(SingletonMeta):

    def __init__(self) -> None:
        self.neural_net_matrix = []
        self.engine : Engine = None
        
        NNetMatrix = [a, b, c]
        engine = Engine(NNetMatrix)
        result = engine.run([[1,2,3], [4,5,6,7]])
        print(result)

    