from CortexBack.utils.SingletonMeta import SingletonMeta
from CortexPackage.src.main_lib import Engine


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
    