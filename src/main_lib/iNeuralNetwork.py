
class INeuralNetwork:

    def __init__(self) -> None:
        # self.shape = (inputShape, outputShape)
        self.input = []
        self.output = []

    def run(self, data):
        self.input = data
        self.output = [i + 1 for i in data]
