from gtts import gTTS
import os
import zipfile


words = [
    "navigate", "satellite", "primitive", "ancestor", "rely", "acute", "magnetic", "dedicate", "pursuit", "disgust", "nutrient", "indispensable", "storage", "expertise", "collector", "scent", "earnest", "obediently", "drill", "economic", "occupation", "initial", "recite", "procedure", "forgetful", "retain", "illustrate", "continent", "vividly", "clarify", "cram", "deadline", "adequate", "foundation", "gap", "session", "diligence", "attribute", "conduct", "detect", "symmetry", "consult", "galaxy", "divert"


]

output_dir = "audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for word in words:
    try:
        tts = gTTS(text=word, lang='en', slow=False)
        filename = os.path.join(output_dir, f"{word}.mp3")
        tts.save(filename)
        print(f"生成音檔：{filename}")
    except Exception as e:
        print(f"生成 {word} 的音檔失敗：{e}")

zip_filename = "gtts_audio_files.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for foldername, subfolders, filenames in os.walk(output_dir):
        for file in filenames:
            filepath = os.path.join(foldername, file)
            zipf.write(filepath, arcname=file)

print(f"Zip 檔案 '{zip_filename}' 已建立，共包含 {len(words)} 個音檔。")
