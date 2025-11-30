import numpy as np
from scipy.fftpack import ifft, fft, fftfreq

resistive_ratio = 0.965
mag_solution = [4.920e-01, 8.326e+00]
phase_solution = [-7.388e-04, 3.960e-01, 5.120e-08]

def fakepower(num, power):
    return np.sign(num)*np.power(np.abs(num), power)

def shift180(num):
    return (num + 180) % 360 - 180

def phase_func(param, freq):
    return param[0] * fakepower(freq, param[1]) + param[2] * freq

def phase_cost(param, masked_real, masked_freqs):
    fake = phase_func(param, masked_freqs)
    ret = np.mean((masked_real - fake)**2)
    return ret

def mag_func(param, freq):
    mag = resistive_ratio*10**(-1*10**(param[0]*(np.log10(np.abs(freq)) - param[1])))
    return mag

#10, 8.5 for pulse
#
def modified_mag_func(param, freq):
    mag = resistive_ratio*10**(-1*10**(param[0]*(np.log10(np.abs(freq)) - param[1]))*modifier([2, 8.5], freq))
    return mag

def mag_cost(param, masked_real, masked_freqs):
    fake = mag_func(param, masked_freqs)
    return np.mean((masked_real - fake)**2)

def transfer_func(freq):
    phase = phase_func(phase_solution, freq)
    phase = np.exp(1j * phase)

    mag = modified_mag_func(mag_solution, freq)

    return mag * phase

def modifier(param, freq):
    ret = 1/(1 + 10**(-param[0]*param[1])*np.abs(freq)**param[0])
    # print(freq[ret > 5550])
    return ret

def inverse_mag_func(param, freq):
    return 1/modified_mag_func(param, freq)

def inverse_transfer_func(freq):
    phase = phase_func(phase_solution, freq)
    phase = -phase
    phase = np.exp(1j * phase)

    mag = inverse_mag_func(mag_solution, freq)

    return mag * phase

def transform(short_signal, time_span):
    freq = fftfreq(len(short_signal), time_span/len(short_signal))
    return ifft(fft(short_signal) * transfer_func(freq))

def inverse_transform(short_signal, time_span):
    freq = fftfreq(len(short_signal), time_span/len(short_signal))
    return ifft(fft(short_signal) * inverse_transfer_func(freq))