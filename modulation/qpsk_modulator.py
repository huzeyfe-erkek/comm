## TODO: finish it

import numpy as np
from numpy import sign as sign

from modulation.abstract_modulator import AbstractModulator

class QpskModulator(AbstractModulator):
    def __init__(self, mapping: np.array = np.r_[0, 1, 3, 2]) -> None:
        super().__init__()
        self.name = "QPSK"
        self.mapping = mapping

    def __call__(self, bits):
        # Check size
        if bits.size % 2: # It must be multiple of 2
            raise AssertionError("Size must be multiple of 2!")

        # Get 
        symbols = 2*bits - 1
        return symbols.astype(int)
