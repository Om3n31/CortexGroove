from NeuralNetwork import NeuralNetwork
from main_lib.iNeuralNetwork import INeuralNetwork


class NeuralNetworkCortex(NeuralNetwork, INeuralNetwork):
    """
    This class inherit from the Neural Network which is the network from the lib.
    It's also inherit from the INeuralNetwork which is the interface to work with the CortexGroove engine.
    """

    def __init__(self, shape):
        super(NeuralNetworkCortex, self).__init__(shape)
        # super(INeuralNetwork, self).__init__()

    def train(self, train_input, train_output):
        """
        Might be useful for later, if we want to train the data dynamically
        :param train_input:
        :param train_output:
        :return:
        """
        super(NeuralNetworkCortex, self).train(train_input, train_output)

    def predict(self, data):
        """
        Return the prediction, but most importantly set the output value
        :param data: is a list of multiple input to test
        :return:
        """
        prediction = super(NeuralNetworkCortex, self).predict(data)
        return prediction
