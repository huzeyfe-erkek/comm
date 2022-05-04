from abc import ABC, abstractmethod

class AbstractDemodulator(ABC):
    '''
    Abstract demodulator

    INPUT:
        symbols - Input symbols

    OUTPUT:
        bits    - Demodulated bits
        
    '''
    def __init__(self) -> None:
        super().__init__()
        self.name = "None"
        
    def __call__(self, symbols):
        cleanSymbols = self.estimateSymbols(symbols)
        return self.demodulateCleanSymbols(cleanSymbols)

    def reset(self):
        # Nothing to be reset
        return

    @abstractmethod
    def estimateSymbols(self, noisySymbols):
        return NotImplemented

    @abstractmethod
    def demodulateCleanSymbols(self, cleanSymbols):
        return NotImplemented
