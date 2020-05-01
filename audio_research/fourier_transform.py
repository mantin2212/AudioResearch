import numpy as np
from operator import itemgetter


from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt

from audio_research.utils.math_utils import RealFunction
from audio_research.wav_file import WavFile


def get_transform(t, samples):
    n = len(samples)

    freqs = fftfreq(n, d=t / n)
    fft_out = fft(samples)
    fft_real = 2.0 * np.abs(fft_out / n)

    mask = freqs > 0

    freqs = freqs[mask]
    fft_real = fft_real[mask]

    return RealFunction(freqs, fft_real)


def get_freqs(path):
    wav_file = WavFile(path)
    fft_output = get_transform(wav_file.get_total_time(), wav_file.get_channel(0))

    return fft_output
