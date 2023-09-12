
# Local creation

from main_lib.iNeuralNetwork import Position
from main_lib.INeuralNetwork import INeuralNetwork
from main_lib.tools import *

class Engine:

    def __init__(self, NeuralNetList) -> None:
        self.neuralNetList = NeuralNetList
        self.layers = []
        for nnLayer in NNetMatrix:
            self.layers.append(Layer(nnLayer))

    def set_layer(self, neural_net, layer_index):
        if self.layers[layer_index] != None:
            self.layers.append(Layer([neural_net]))
        else :
            self.layers[layer_index].NNList.append(neural_net)

    def run(self, inputData):
        data = inputData
        output_data = []
        first_nn = [i for i in self.neuralNetList if i.position is Position.FIRST]
        
        for index, nn in enumerate(first_nn):
            nn.predict(data[index])
            output_data.append(nn.output)

        for layer in self.layers:
            layer.run(data)
            data = layer.output
        print(data)
        return data

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
        
        self.output = flatten_list(outputTemp)


if __name__ == '__main__':
    a = INeuralNetwork()
    b = INeuralNetwork()
    c = INeuralNetwork()
    a.name = "a"
    b.name = "b"
    c.name = "c"

    NNetMatrix = [[a, b], [c]]
    engine = Engine(NNetMatrix)
    engine.run([[1,2,3], [4,5,6,7]])