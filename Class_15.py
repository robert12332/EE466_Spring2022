import numpy as np
import matplotlib.pyplot as plt

Fs = 300  # sample rate
Ts = 1 / Fs  # sample period
print(Ts)

N = 2048
t = Ts * np.arange(N)
x = np.exp(1j * 2 * np.pi * 50 * t)

noise = (np.random.rand(N) + 1j * np.random.rand(N)) / np.sqrt(2)
noise_pwr = 2

recievedX = x + noise * np.sqrt(noise_pwr)

PSD = (np.abs(np.fft.fft(recievedX))/N)**2

PSD_log = 10.0*np.log10(PSD)
PSD_shifted = np.fft.fftshift(PSD_log)

f= np.arange(Fs/-2.0, Fs/2.0, Fs/N)

plt.plot(f,PSD_shifted)
plt.xlabel("Frequency in Hz")
plt.show()