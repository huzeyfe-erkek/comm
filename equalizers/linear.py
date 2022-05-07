import numpy as np
from scipy.linalg import toeplitz
from scipy.signal import convolve

def zeroForcing(channelTaps: np.array, desiredLen : int = 0):
    '''
    Tap solution from given channel vector. Delay == 0

    Source: "Principles of Mobile Communication", Gordon L. Stüber, Section 7.4.1 ZERO-FORCING.
    It is not copy-paste implementation. Please, do not expect line-by-line match.

    INPUT:
        channelTaps     - Overall channel vector

        desiredLen      - Default length is channelTaps.shape[0]. Text books may use 2*d2-1 length filter where d2 == (channelTaps.shape[0] - 1)

    OUTPUT:
        equalizerTaps   - FIR taps

    '''
    # Check desired len
    if (desiredLen == 0):
        desiredLen = channelTaps.shape[0]
    elif (desiredLen > 0): # TODO: Check peak distortion.
        None
    else: # (desiredLen < 0)
        raise AssertionError("Desired tap is negative")

    # Get Toeplitz matrix
    firstCol = np.r_[[channelTaps[0]], np.zeros(desiredLen-1)]
    if (channelTaps.shape[0] < desiredLen):
        firstRow = np.r_[channelTaps, np.zeros(desiredLen - channelTaps.shape[0])]
    else:
        firstRow = np.r_[channelTaps[0:desiredLen]]

    C = toeplitz(firstCol, firstRow) # Stüber used letter G instead of C. And he also used d1 metric which is the greatest magnitude element

    # Right side of ZF equalizer weight equation
    #q = np.r_[np.zeros(desiredLen/2-1), [1], np.zeros(desiredLen/2-1)] # It is complicating things since filter length is variable.
    q = np.r_[[1], np.zeros(desiredLen-1)] # Delay == 0

    # Solve for ZF equalizer weights
    wZf, resid, rank, s = np.linalg.lstsq(C.T, q, rcond=-1) # Left matrix division, rcond is about internals of python

    return wZf

def minimumMeanSquareError(channelTaps: np.array, N0: float, desiredLen : int = 0):
    '''
    Tap solution from given channel vector.

    Source: "Principles of Mobile Communication", Gordon L. Stüber, Section 7.4.2 MINIMUM MEAN-SQUARE-ERROR (MMSE). And, MATLAB

    INPUT:
        channelTaps     - Overall channel vector

        N0              - Noise power

        desiredLen      - Default length is channelTaps.shape[0]. Text books may use 2*d2-1 length filter where d2 == (channelTaps.shape[0] - 1)

    OUTPUT:
        equalizerTaps   - FIR taps

    '''
    # Common
    channelTaps.reshape(-1)
    cLen = channelTaps.shape[0]

    # Check desired len
    if (desiredLen == 0):
        desiredLen = cLen
    elif (desiredLen > 0):
        None
    else: # (desiredLen < 0)
        raise AssertionError("Desired tap is negative")

    # Get autocorreleation sequence
    channelTapsFlipped = np.conj(np.flipud(channelTaps))
    r = convolve(channelTaps, channelTapsFlipped)
    offset = cLen - 1
    r = r[offset::] # Delete negative lags

    # Add noise power
    r[0] += N0

    if (desiredLen <= cLen):
        r = r[:desiredLen] # Delete negative lags. And, delete from the end if the length is depicted
    else:
        r = np.r_[r, np.zeros(desiredLen - cLen)]

    # Get autocorrelation matrix
    Rxx = toeplitz(r, np.conj(r)) # Stüber used symbol Mv instead (vice-versa)

    # Get right hand-side of the Wiener-Hoph equation
    Rxd = np.r_[np.conj(np.flipud(channelTaps)), [0]] # Stüber used symbol vx_h instead (vice-versa). AND, I dont know why this zero is need to be added (I really wonder the reason).
    RxdLen = Rxd.shape[0]
    if (desiredLen < RxdLen):
        Rxd = Rxd[(RxdLen-desiredLen)::]
    elif (desiredLen > RxdLen):
        Rxd = np.r_[Rxd, np.zeros(desiredLen - RxdLen)]
    Rxd.reshape(-1, 1)

    # Solve the linear equation
    wMmse, resid, rank, s = np.linalg.lstsq(Rxx, Rxd, rcond=-1) # Left matrix division, rcond is about internals of python

    return wMmse