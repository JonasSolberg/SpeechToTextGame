from django.conf.locale import sr
from pydub import AudioSegment
import soundfile as sf
import soundfile as s
import pyrubberband as pyrb
sound = AudioSegment.from_mp3("../outputAudio10000.mp3")
sound.export("file.wav", format="wav")



data, samplerate = sf.read('file.wav')



# Play back at 1.5X speed
y_stretch = pyrb.time_stretch(y, sr, 1.5)
# Play back two 1.5x tones
y_shift = pyrb.pitch_shift(y, sr, 1.5)
sf.write("file.wav", y_stretch, sr, format='wav')

sound = AudioSegment.from_wav("file.wav")
sound.export("mp3fromatfile.mp3", format="mp3")