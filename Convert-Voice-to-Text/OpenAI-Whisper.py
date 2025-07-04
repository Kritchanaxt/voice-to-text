import whisper
import time

start_time = time.time()

print("กำลังโหลดโมเดล...")
model = whisper.load_model("tiny")  
print("โหลดเสร็จใน %.2f วินาที" % (time.time() - start_time))

print("ถอดข้อความจากเสียง...")
result = model.transcribe("digital-ink.m4a") 

print("== RAW RESULT ==")
print(result)

print("\nภาษา:", result["language"])
print("\nข้อความจากเสียง:")
print(result["text"])
