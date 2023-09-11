
from enum import Enum

class Position(Enum):
    FIRST = 0
    MIDDLE = 1
    LAST = 2

class State(Enum):
    IDLE = 0
    WORKING = 1


class INeuralNetwork:

    def __init__(self, position=Position.MIDDLE) -> None:
        # self.shape = (inputShape, outputShape)
        self.position = position
        self.next_NN = [] # Next neural network list
        self.input = []
        self.output = []

    def predict(self, data):
        self.input = data
        self.output = [i + 1 for i in data]

