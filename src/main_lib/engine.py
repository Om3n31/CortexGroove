
# Local creation

from src.main_lib.iNeuralNetwork import INeuralNetwork

class Engine:

    def __init__(self, NNetMatrix) -> None:
        self.layers = []
        for nnLayer in NNetMatrix:
            self.layers.append(Layer(nnLayer))

    def run(self, inputData):
        data = inputData
        for layer in self.layers:
            layer.run(data)
            data = layer.output
        print(data)

class Layer:

    def __init__(self, NNList) -> None:
        self.NNList = NNList
        self.output = None
        self.input = None

    def run(self, inputData):
        self.input = inputData
        outputTemp = []
        for index, nn in enumerate(self.NNList):
            if isinstance(inputData[0], list):
                nn.run(inputData[index])
            else:
                nn.run(inputData)
            outputTemp.append(nn.output)
        
        self.output = self.flatten_list(outputTemp)

    def flatten_list(self, lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(self.flatten_list(item))
            else:
                result.append(item)
        return result


if __name__ == '__main__':
    a = INeuralNetwork(3,2)
    b = INeuralNetwork(4,4)
    c = INeuralNetwork(6,2)
    a.name = "a"
    b.name = "b"
    c.name = "c"

    NNetMatrix = [[a, b], [c]]
    engine = Engine(NNetMatrix)
    engine.run([[1,2,3], [4,5,6,7]])