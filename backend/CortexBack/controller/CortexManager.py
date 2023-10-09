# from utils.SingletonMeta import SingletonMeta
from CortexBack.utils.SingletonMeta import SingletonMeta
from main_lib.Engine import Engine
from main_lib.iNeuralNetwork import INeuralNetwork, Position


class CortexManager(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.neural_net_matrix = []
        self.engine : Engine = None
        
        # engine = Engine(NNetMatrix)
        # result = engine.run([[1,2,3], [4,5,6,7]])
        # print(result)

    def start(self, data):
        self.engine = Engine(self.neural_net_matrix)
        result = self.engine.run(data)
        print(result)
        return result
    