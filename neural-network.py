import numpy as np


#x = hours (sleeping, studying), y = test score
x = np.array(([2,9],[1,5],[3,6]), dtype=float)
y = np.array(([92],[86],[89], dtype=float))

#scale units
X = X/np.amax(X, axis=0)
y = y/100

class NeuralNetwork(object):
    def __init__(self):
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3

        
