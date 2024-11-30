import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Charger le fichier audio
file_path = "ch3.wav"
signal, sr = librosa.load(file_path, sr=None)  # sr=None pour garder la fréquence d'origine

# Afficher le signal dans le domaine temporel
plt.figure(figsize=(10, 4))
librosa.display.waveshow(signal, sr=sr)
plt.title("Signal audio (domaine temporel)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.show()

# Calculer la FFT
fft = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(fft), 1/sr)  # Calcul des fréquences
magnitude = np.abs(fft)  # Amplitude spectrale

# Visualiser le spectre (uniquement pour les fréquences positives)
plt.figure(figsize=(10, 4))
plt.plot(freqs[:len(freqs)//2], magnitude[:len(magnitude)//2])
plt.title("Spectre du signal (FFT)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
