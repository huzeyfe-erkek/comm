import numpy as np
from adaptive_filters.abstract_adaptive_filter import AbstractAdaptiveFilter

class Rls(AbstractAdaptiveFilter):
    '''
    Recursive Least Squares (RLS) algorithm for real signals.
    '''

    def __init__(self, L : int, lmbda : float = 0.999, delta : float = 0.01, w = None) -> None:
        '''
        Constructor

        INPUT:
            L       - Filter length
            
            lmbda   - Forgetting factor

            delta   - Regularization term 
            
            w       - Input weight vector. If == None, zero vector will be initialized. Its length is same as xk.
        '''
        super().__init__(L)
        self.lmbda = lmbda
        self.lmbda_inv = 1/lmbda
        self.delta = delta
        self.P = None
        self.reset()

    def reset(self):        
        '''
        Clear weights and P
        '''
        super().reset()
        self.P = np.eye(self.L)*self.delta

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
        ek = dk - np.dot(u.T, self.w)

        # Calculate gain
        P_u = np.dot(self.P, u) 
        g = P_u / (self.lmbda + np.dot(u.T, P_u))

        # Calculate new weights
        self.w = self.w + ek*g

        # Calculate new P vector
        self.P = self.lmbda_inv*(self.P - np.outer(g, np.dot(u.T, self.P)))
        
        return self.w, ek
