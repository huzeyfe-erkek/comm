import numpy as np

def convert3DTensor(input: np.array):
    '''
    Convert 1D or 2D array to 3D array.

    INPUT:
        input       - 1D or 2D array

    OUTPUT:
        output      - 3D array

    '''
    if input.ndim == 1:
        return input.reshape(input.shape[0], 1, 1)
    elif input.ndim == 2:
        return input.reshape(input.shape[0], input.shape[1], 1)
    raise AssertionError("Input dim[" + input.dim + "] is not 1 or 2")