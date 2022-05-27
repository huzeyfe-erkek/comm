## TODO: finish it

import numpy as np
from numpy import sign as sign

from modulation.abstract_demodulator import AbstractDemodulator

class QpskDemodulator(AbstractDemodulator):
    def __init__(self) -> None:
        super().__init__()
        self.name = "QPSK"
    
    # Override
    def estimateSymbols(self, noisySymbols):
        cleanSymbols = sign(noisySymbols)
        for i in range(cleanSymbols.size):
            if cleanSymbols[i] == 0:
                cleanSymbols[i] = -1
        return cleanSymbols

    # Override
    def demodulateCleanSymbols(self, cleanSymbols):
        bits = (cleanSymbols + 1) / 2
        return bits.astype(int)
