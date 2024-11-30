import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Charger le fichier audio
file_path = "ch3.wav"
signal, sr = librosa.load(file_path, sr=None)  # sr=None pour garder la fréquence d'origine

# Calculer le spectrogramme
stft = librosa.stft(signal)  # Short-Time Fourier Transform
spectrogram = librosa.amplitude_to_db(np.abs(stft), ref=np.max)

# Visualiser
plt.figure(figsize=(10, 6))
librosa.display.specshow(spectrogram, sr=sr, x_axis='time', y_axis='log', cmap='magma')
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogramme")
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.show()
