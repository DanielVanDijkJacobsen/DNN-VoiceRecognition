import pyaudio
import wave


def gather_sound(time, output_name):
    p = pyaudio.PyAudio()
    chunk = 1024
    sound_format: int = pyaudio.paInt16
    channels = 2
    rate = 44100
    stream = p.open(format=sound_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    wave_output_filename = (output_name + ".wav")
    print("* recording")
    frames = []
    for i in range(0, int((rate / chunk) * time)):
        data = stream.read(chunk)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(wave_output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sound_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()


gather_sound(5, "test")
