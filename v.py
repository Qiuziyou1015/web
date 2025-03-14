from gtts import gTTS
import os
import zipfile


words = [
    "workforce", "industrialized", "industrialize", "dramatic", "flourish", "fade",
    "prominence", "prominent", "generation", "decade", "physical", "symbolize",
    "symbolic", "rural", "specialize", "specialty", "modify", "boom", "manufacturing",
    "manufacturer", "era", "significance", "significant", "apprentice", "alter",
    "reflect", "reflection", "reflective", "transition", "transit", "category",
    "categorize", "arise",
    "journalist", "journal", "genuine", "neglected", "neglect", "misunderstood",
    "misunderstand", "promote", "promotion", "assumption", "assume", "discrimination",
    "discriminate", "transformation", "compassionate", "compassion", "alternatively",
    "alternative", "flee", "extraordinary", "remarkable", "remark", "glimpse",
    "undoubtedly", "dissolve", "replace", "replacement", "sweat", "beneath",
    "disability", "immigrant", "immigrate", "retire", "retirement", "initially",
    "initial", "norms",
    "bang", "insult", "addict", "addicted", "stare", "stride", "mentor", "zone",
    "locker", "toss", "aside", "breeze", "absolute", "chaos", "rival", "assign",
    "assignment", "translate", "translation", "trauma", "mighty", "sword", "release",
    "hatred", "aggressive", "blossom", "dare"
]

output_dir = "gtts_audio_files"
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
