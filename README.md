# Digital Communications Library

Communication library focused on channel equalization. It doesn't have a definite goal and will be updated as needed.

## Current Modules
### Adaptive Filers
* LMS, NLMS
* RLS

### Equalizers
* Static Linear Equalizer: ZF, MMSE (Wiener) tap solution

### Modulators
* BPSK

### Random Variable (RV) Generators from Uniform Distribution
* Gaussian RV
* Rayleigh RV
* Nakagami-m (m can be choosen integer or half-integer)
* Gamma RV
* Generalized K RV

### Examples
* End-to-end Linear Equalizer comparison. Used techniques: ZF, MMSE and LMS
* Equalizer comparison based discrete channel model (still developing)
* QPSK BER simulation on fading channel

### Test
* Currently ipynb files are used for testing

## TODO
* More equalizers, DFE, MLSE and Machine Learning based equalizers
* Using a test framework
* Various (de)modulators such as QPSK, PSK, DPQSK
* Add references

## Known Issues
* In equalizer module, filter delay mechanism seems unhealty