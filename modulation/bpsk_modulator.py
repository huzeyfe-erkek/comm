import numpy as np
from numpy import sign as sign

from modulation.abstract_modulator import AbstractModulator

class BpskModulator(AbstractModulator):
    def __init__(self) -> None:
        super().__init__()
        self.name = "BPSK"

    def __call__(self, bits):
        symbols = 2*bits - 1
        return symbols.astype(int)
