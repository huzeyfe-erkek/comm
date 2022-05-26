from abc import ABC, abstractmethod
#from multipledispatch import dispatch TODO
import numpy as np

class AbstractAdaptiveFilter(ABC):
    def __init__(self, L : int) -> None:
        '''
        Constructor

        INPUT:
            L       - Filter length                    
        '''
        super().__init__()
        self.L = L
        self.w = None
        AbstractAdaptiveFilter.reset(self)
                
    def reset(self):
        '''
        Clear weights
        '''
        self.w = np.zeros((self.L, 1))

    @abstractmethod
    def evalChunk(self, xk, dk):
        '''
        Abstract method for adaptive filter
        '''
        pass

    def eval(self, x, d, iterMax : int = -1):
        '''
        Calculates for weights for given vectors.

        INPUT:
            x       - Input vector

            d       - Output values in vector

            iterMax - Iteration limit

        OUTPUT:
            w       - Output weight

            e       - Output errors in a vector
        '''
        # Get iteration quantity
        iterAvailable = min(x.shape[0], d.shape[0]) - int(self.L/2)
        if (iterMax == -1):
            iterMax = iterAvailable
        else:
            iterMax = min(iterMax, iterAvailable)

        # Common variables
        e = np.zeros((iterMax, 1))

        # Call adaptive algorithm  
        for k in range(iterMax):
            xk = x[k : k+self.L]
            w, e[k] = self.evalChunk(xk, d[k])

        return self.w, e  
