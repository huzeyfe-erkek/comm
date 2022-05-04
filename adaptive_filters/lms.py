import numpy as np
from adaptive_filters.abstract_adaptive_filter import AbstractAdaptiveFilter

class Lms(AbstractAdaptiveFilter):
    '''
    Least Mean Squares (LMS) algorithm for real signals.
    '''

    def __init__(self, L : int, mu : float, algorithm : str = "lms") -> None:
        '''
        Constructor

        INPUT:
            L       - Filter length
            
            mu      - Convergence coefficient

            algorithm - lms or nlms
        '''
        super().__init__(L)
        self.mu = mu
        self.algorithm = algorithm
        self.reset()
    
    def evalChunk(self, xk, dk):
        '''
        Calculates one iteration for the given chunk.

        INPUT:
            xk      - Input chunk [xk(0); xk(1); ...; xk(L-1)]. Shape is (L,1)

            dk      - Output value. Shape is (1,1)

        OUTPUT:
            w       - Output weights

            ek      - Output error
        '''
        # Flip input array
        u = np.flipud(xk).reshape(-1,1)

        # Get error
        ek = dk - np.dot(self.w.T, u)

        # Update weights
        if self.algorithm == "nlms":
            self.w = self.w + self.mu*ek*u/(np.dot(u.T, u))
        else:
            self.w = self.w + self.mu*ek*u
        
        return self.w, ek
        