from abc import ABC, abstractmethod

class AbstractModulator(ABC):
    '''
    Abstract modulator

    INPUT:
        bits    - Input bits

    OUTPUT:
        symbols - Modulated symbols

    '''
    def __init__(self) -> None:
        super().__init__()
        self.name = "None"

    @abstractmethod
    def __call__(self, bits):
        pass
