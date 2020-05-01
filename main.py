



def main():
    plt.plot(get_freqs(r"..\resources\0\1000hz.wav"))





def main():
    fft_output = get_freqs(r"..\resources\0\two_freqs.wav")
    r = find_peak_points(fft_output, 600)
    print(r)


def main():
    path = r"..\resources\0\out.wav"
    wav = WavFile(path)
    samples = wav.get_channel(0)

    domain = wav.domain()
    plt.plot(domain, samples)
    plt.show()


if __name__ == '__main__':
    main()
