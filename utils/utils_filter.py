#------------------------------------------------------------------------------#
# All inputs MUST be column vector. Otherwise undefined behaviour
#------------------------------------------------------------------------------#

from scipy.signal import convolve

def filterB(b, x, offset : int = 0):
    '''
    FIR filter. Output offset can be tuned.

    INPUT:

        b       - FIR filter coefficients

        x       - Input signal

        offset  - Output offset

    OUTPUT:

        y       - Filtered signal
    '''
    b = b.reshape(-1)
    x = x.reshape(-1)
    y = convolve(b, x).reshape(-1,1)
    return y[offset:x.size + offset]