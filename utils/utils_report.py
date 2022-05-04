import numpy as np
from numpy import log10 as log10
from numpy import floor as floor
from numpy import mod as mod

from modulation.abstract_demodulator import AbstractDemodulator
from utils.utils_waveform import power

def number2SciFormatStr(num : float):
    '''
    Represent given number as decimal power formatted string

    INPUT:
        num     - Any number

    OUTPUT:
        sciStr  - Scientific formatted string representation
    '''
    # Zero check
    if (num == 0.0):
        return "0.0e0"
        
    decimalPower = log10(num)
    decimalPowerFloor = floor(decimalPower)
    residual = mod(decimalPower, 1)
    sciStr = str(10**residual) + "e" + str(decimalPowerFloor.astype(int))
    return sciStr

def symbolErrorRate(recv, ref):
    '''
    Calculate given symbols' error rate

    INPUT:
        recv    - Estimated symbols

        ref     - Reference symbols

    OUTPUT:
        ser     - SER rate
    '''
    _ref = ref.reshape(-1)
    _recv = recv.reshape(-1)
    _s = _ref.size
    val = 0.0
    for k in range(0, _s):
        if (ref[k] != recv[k]):
            val += 1.0 
    return val/_s

def errorVectorMagnitude(recv, ref, method : str = "rms"):
    '''
    Calculate given symbols' EVM

    INPUT:
        recv    - Received noisy symbols

        ref     - Reference symbols

        method  - Currently only RMS is supported

    OUTPUT:
        evm     - EVM
    '''
    _ref = ref.reshape(-1)
    _recv = recv.reshape(-1)

    # Custom switch-case
    if False: # Add new EVM methods here
        AssertionError("Unexpected@errorVectorMagnitude")
    else: # str=="rms" is default
        return np.sqrt(power(_ref-_recv)/power(_ref))*100

def linkReport(recvSyms, refSyms, demodulator : AbstractDemodulator):
    '''
    Prints SER and EVM

    INPUT:
        recvSyms - Received noisy symbols

        refSyms - Reference symbols

        demodulator - Reference demodulator object

    '''
    # Get estimated symbols
    estimatedSyms = demodulator.estimateSymbols(recvSyms)

    # Get SER value
    ser = symbolErrorRate(estimatedSyms, refSyms) 
    
    # Count total symbol errors
    lenSyms = recvSyms.size  
    errSyms = 0 
    for k in range(0, lenSyms):
        if (estimatedSyms[k] != refSyms[k]):
            errSyms += 1 

    # Get EVM
    evm = errorVectorMagnitude(recvSyms, refSyms)

    # Demodulate bits
    demodulator.reset()
    refBits = demodulator(refSyms)
    demodulator.reset()
    recvBits = demodulator(recvSyms)
    
    # Get BER value
    ber = symbolErrorRate(recvBits, refBits) 

    # Count bit errors
    lenBits = recvBits.size  
    errBits = 0 
    for k in range(0, lenBits):
        if (recvBits[k] != refBits[k]):
            errBits += 1
        
    # Print report        
    print("Link Report (" + demodulator.name + "):")
    print("    SER, " + str(number2SciFormatStr(ser)) + ", (" + str(errSyms) + "/" + str(lenSyms) + ")")
    print("    BER, " + str(number2SciFormatStr(ber)) + ", (" + str(errBits) + "/" + str(lenBits) + ")")
    print("    EVM, " + str(evm) + " [RMS]")