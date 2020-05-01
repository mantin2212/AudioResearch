from math import ceil
import numpy as np

import matplotlib.pyplot as plt
import wave


class WavFile(object):
    DEFAULT_FRAME_CHUNK = 1024

    def __init__(self, file_path):
        self.path = file_path
        self.file = wave.open(file_path)

    def get_samples(self, chunk_size=DEFAULT_FRAME_CHUNK):
        """
        Read the sample list from the file.
        :param chunk_size: WAV frame chunk size.
        :return: A list of the wav file samples.
        :rtype: list
        """
        wav_file = self.file

        chunk_number = ceil(wav_file.getnframes() / chunk_size)
        sample_width = wav_file.getsampwidth()

        result = []
        for i in range(chunk_number):
            result += self.parse_frames(wav_file.readframes(chunk_size), sample_width)

        return result

    def get_channel(self, channel_idx):
        samples = self.get_samples()
        return samples[channel_idx::self.file.getnchannels()]

    @staticmethod
    def parse_frames(frame_bytes, sample_width):
        """
        Parsing wav frames according to the file sample width.
        :param list frame_bytes: Raw WAV frames to parse.
        :param int sample_width: The wav file sample width (bytes per sample).
        :return: The correct sample values of the wav frames.
        :rtype: list
        """
        frame_values = [frame_bytes[i: i + sample_width] for i in range(0, len(frame_bytes), sample_width)]
        return [int.from_bytes(val, byteorder='little', signed=True) for val in frame_values]

    def get_total_time(self):
        return self.file.getnframes() / self.file.getframerate()

    def domain(self):
        return np.linspace(0, self.get_total_time(), self.file.getnframes())
