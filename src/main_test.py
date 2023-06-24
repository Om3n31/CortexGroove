import random

import numpy as np
from numpy import array

from NeuralNetwork import NeuralNetwork
from NeuralNetworkCortex import NeuralNetworkCortex

def function(input_data):
    return (input_data[0] / 2) + input_data[1] - input_data[2]

def createSet():
    # Generate a data set
    num_samples = 10000
    input_data = np.random.rand(num_samples, 3)
    output_data = np.array([function(x) for x in input_data])

    # Split the data into train and test
    train_input = input_data[:8000]
    train_output = output_data[:8000]

    test_input = input_data[8000:]
    test_output = output_data[8000:]
    return train_input, train_output, test_input, test_output


train_input, train_output, test_input, test_output = createSet()
shape = [3,1] # It means that the model will take a list of 3 element in input and will output one element
nn = NeuralNetworkCortex(shape)
nn.train(train_input, train_output)
nn.test(test_input, test_output)
prediction_data = [1,0,1]
print(f"Result of {prediction_data} is {nn.predict([prediction_data])}")

# a = NeuralNetworkCortex(3, 2)
# b = NeuralNetworkCortex(4, 4)
# c = NeuralNetworkCortex(6, 2)
# a.name = "a"
# b.name = "b"
# c.name = "c"
#
# NNetMatrix = [[a, b], [c]]
# engine = Engine(NNetMatrix)
# engine.run([[1, 2, 3], [4, 5, 6, 7]])