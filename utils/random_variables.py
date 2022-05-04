#------------------------------------------------------------------------------#
# Generating RVs from uniformly distribured RV
#
# Source: Istanbul Technical University (ITU)
#Lecture Notes from TEL514 Modulation and Coding in Wireless Communications
#------------------------------------------------------------------------------#

# Dependencies
import numpy as np

pi = np.pi
from numpy import log as log
from numpy import cos as cos
from numpy import sqrt as sqrt

# Gaussian distributed RV with Box-Muller Method
def gaussian_rv(mean, variance, length):
    # Uniform RVs
    U_1 = np.random.uniform(0, 1, length)
    U_2 = np.random.uniform(0, 1, length)

    # Generating from rayleigh    
    return mean + sqrt(variance * (-2) * log(U_1)) * cos(2 * pi * U_2)   

# Rayleigh distributed RV
# omega = 2 * variance
def rayleigh_rv(omega, length):
    U_1 = np.random.uniform(0, 1, length)

    return sqrt(-omega * log(U_1))

# Nakagami-m R.V. for integer m values
def nakagami_int_m_rv(m, omega, length):
    # Temel Parametreler
    omega_rayleigh = omega / m
    output = np.zeros(length)
    
    # Rayleigh'lerin uretimi ve toplanmasi
    for rayleigh_index in range(m):
        output = output + rayleigh_rv(omega_rayleigh, length)**2
        
    # Karekok alinmasi ve uretimin tamamlanmasi
    return sqrt(output)

# Nakagami-m R.V. for half-integer m values
def nakagami_half_int_m_rv(m, omega, length):
    # Temel Parametreler
    variance_gauss = omega / 2 / m
    output = np.zeros(length)
    
    # Gauss'lerin uretimi ve toplanmasi
    for gauss_index in range(int(2*m)):
        output = output + gaussian_rv(0, variance_gauss, length)**2
    
    # Karekok alinmasi ve uretimin tamamlanmasi
    return sqrt(output)

# Gamma R.V.
# Teta -> y_0
def gamma_rv(k, y_0, length):
    # Temel Parametreler
    variance_gauss = y_0 / 2
    output = np.zeros(length)
    
    # Gauss'lerin uretimi ve toplanmasi
    for gauss_index in range(int(2*k)):
        output = output + gaussian_rv(0, variance_gauss, length)**2
  
    return output
    
# Generalized-K R.V.
def generalized_k_rv_from_double_nakagami(power, k, m, length):
    return nakagami_half_int_m_rv(m, sqrt(power), length) * nakagami_half_int_m_rv(k, sqrt(power), length);