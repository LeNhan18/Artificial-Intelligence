import speech_recognition as sr
from pydub import AudioSegment

# Đường dẫn tệp âm thanh
mp3_path = "C:\\Users\\Admin\\Downloads\\Part2 (Day 8+9+10)\\DAY 10.mp3"
wav_path = "C:\\Users\\Admin\\Downloads\\Part2 (Day 8+9+10)\\DAY_10.wav"

# Chuyển đổi từ MP3 sang WAV
try:
    print("Đang chuyển đổi MP3 sang WAV...")
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
    print("Chuyển đổi thành công!")
except Exception as e:
    print(f"Lỗi khi chuyển đổi: {e}")
    exit()

# Nhận diện giọng nói
recognizer = sr.Recognizer()
try:
    with sr.AudioFile(wav_path) as source:
        print("Đang đọc file âm thanh...")
        audio_data = recognizer.record(source)  # Đọc toàn bộ tệp âm thanh
        print("Đang nhận diện giọng nói...")
        text = recognizer.recognize_google(audio_data, language="en-US")
        print("Nhận diện thành công:", text)
except sr.UnknownValueError:
    print("Không thể nhận diện nội dung.")
except sr.RequestError as e:
    print(f"Lỗi khi kết nối với Google API: {e}")
except Exception as e:
    print(f"Lỗi khác: {e}")