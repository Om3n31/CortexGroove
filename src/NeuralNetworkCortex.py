from UserNeuralNetwork  import UserNeuralNetwork
from main_lib.INeuralNetwork import INeuralNetwork


class NeuralNetworkCortex(UserNeuralNetwork, INeuralNetwork):
    """
    This class inherit from the Neural Network which is the network from the lib.
    It's also inherit from the INeuralNetwork which is the interface to work with the CortexGroove engine.
    """

    def __init__(self, shape):
        super(NeuralNetworkCortex, self).__init__(shape)
        # super(INeuralNetwork, self).__init__()

    def train(self, train_input, train_output, epochs=10):
        """
        Might be useful for later, if we want to train the data dynamically
        :param epochs:
        :param train_input:
        :param train_output:
        :return:
        """
        super(NeuralNetworkCortex, self).train(train_input, train_output, epochs)

    def predict(self, data):
        """
        Return the prediction, but most importantly set the output value
        :param data: is a list of multiple input to test
        :return:
        """
        prediction = super(NeuralNetworkCortex, self).predict(data)
        print(f"Input data : {data}, result : {prediction.tolist()}")
        return prediction.tolist()

    def run(self, data):
        self.output = self.predict([data])
