#------------------------------------------------------------------------------#
# All inputs MUST be column vector. Otherwise undefined behaviour
#------------------------------------------------------------------------------#

import numpy as np
from scipy import signal as signal

def upsample(x, N):
    '''
    Upsample given column vector with zero. Following script from scipy can also be used: 

    INPUT:
        x       - Column vector

        N       - Upsample rate 
    
    OUTPUT:
        xU      - Upsampled signal
    '''
    # Using scipy
    return signal.upfirdn(signal.unit_impulse(N), x, N)
    ''' OLD METHOD
    # Create zero filled array
    r = np.zeros((x.reshape(-1,1).shape[0]*N,1))
    
    # Replace values and return
    r[::N] = x.reshape(-1,1)
    return r
    '''
    
def energy(waveform):
    '''
    Calculate given waveform's energy

    INPUT:
        waveform - Column vector
    
    OUTPUT:
        e       - Energy
    '''
    return np.sum(np.dot(waveform.reshape(-1), waveform.conj().reshape(-1)))

def power(waveform):
    '''
    Calculate given waveform's power

    INPUT:
        waveform - Column vector
    
    OUTPUT:
        e       - Power
    '''
    return energy(waveform)/waveform.size
