import numpy as np
import matplotlib.pyplot as plt
Fs = 500 # sample rate Based on the coding example found in the PDF from Question 1,
#assume that your sampling rate is 500 sample/sec.

Ts = 1/Fs # sample period
N = 2048 # number of samples to simulate still 2048
t = Ts*np.arange(N)

#Generate a signal S1 with a number of samples equal 2048, S1 is a sinusoidal signal with a frequency of 100 HZ.
S1 = 200* np.exp(1j*2*np.pi*100*t) # simulates sinusoid at 100 Hz exp(j2pift)
S2 = 20* np.exp(1j*2*np.pi*200*t) # simulates sinusoid at 200 Hz exp(j2pift)

# Add the two signals together to create a combined signal named TransmittedX
TransmittedX = S1+S2

#generate a random noise signal named noise
noise = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) # complex noise with unity power

#Now, add the random noise signal to the TransmittedX
#The output is a new signal ReceivedX.
noise_power = 2
ReceivedX = noise * np.sqrt(noise_power) + TransmittedX

#Calculate the power spectrum density (PSD) of the signal ReceivedX
PSD = (np.abs(np.fft.fft(ReceivedX))/N)**2

#Convert to Log scale
PSD_log = 10.0*np.log10(PSD)

#Shift the log scale
PSD_shifted = np.fft.fftshift(PSD_log)

#Plot the spectrums
f = np.arange(Fs/-2.0, Fs/2.0, Fs/N) # start, stop, step
plt.plot(f, PSD_shifted)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.show()
plt.savefig('Q2_Fs500_newAmplitudes.png')