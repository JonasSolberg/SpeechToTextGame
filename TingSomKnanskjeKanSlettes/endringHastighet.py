import librosa
import pyrubberband
import soundfile as sf

y, sr = librosa.load(Users/jonas/PycharmProjects/SpeechToText/konvertert.wav, sr=None)
y_stretched = pyrubberband.time_stretch(y, sr, 1.5)
sf.write(analyzed_filepath, y_stretched, sr, format='wav')

def change_audioseg_tempo(audiosegment, tempo, new_tempo):
    y = np.array(audiosegment.get_array_of_samples())
    if audiosegment.channels == 2:
        y = y.reshape((-1, 2))

    sample_rate = audiosegment.frame_rate

    tempo_ratio = new_tempo / tempo
    print(tempo_ratio)
    y_fast = pyrb.time_stretch(y, sample_rate, tempo_ratio)

    channels = 2 if (y_fast.ndim == 2 and y_fast.shape[1] == 2) else 1
    y = np.int16(y_fast * 2 ** 15)

    new_seg = pydub.AudioSegment(y.tobytes(), frame_rate=sample_rate, sample_width=2, channels=channels)

    return new_seg
