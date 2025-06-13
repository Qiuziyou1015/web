from gtts import gTTS
import os
import zipfile


words = [
    "virtual", "entertainer", "entertain", "entertainment", "utilize", "content", "contents", "viewer", "notable", "popularity", "adventure", "frequently", "frequent", "frequency", "constant", "subscriber", "subscribe", "debut", "dynamic", "bond", "comment", "chat", "companionship", "companion", "loyal", "loyalty", "accessibility", "accessible", "visa", "notification", "notify", "signal", "lively", "span", "ecosystem", "nuclear", "genius", "atomic", "atom", "bomb", "invasion", "invade", "horror", "document", "invent", "invention", "inventor", "weapon", "tension", "tense", "wrestle", "stunning", "stun", "audio", "capture", "subjective", "ethical", "portray", "explosion", "explosive", "explode", "quote", "destroyer", "destroy", "destruction", "realization", "profound", "consequence", "weave", "renewed", "renew", "implication", "perception", "perceive", "random", "attribute", "mystery", "mysterious", "clue", "shadow", "surrounding", "surroundings", "surround", "interpretation", "interpret", "infer", "deceive", "depict", "dimly", "dim", "illuminate", "theory", "speculate", "noticeable", "blurred", "blur", "outline", "faint", "concentrate", "concentration", "comprehend", "comprehension", "controversial", "controversy", "contemplate", "objective", "vulnerable", "prevention", "translate", "occupy", "promising", "persuasive", "blossom", "phenomenon", "initially", "fleeting", "celebration", "blooming", "appreciation", "involve", "associate", "priority", "daylight", "cherish", "flee", "refugee", "unprecedented", "rural", "drought", "infrastructure", "reservoir", "scenario", "iconic", "engaging", "remarkable", "route", "stall", "performer", "reflection", "district", "landmark", "spectacular", "behavior", "access", "marine", "mammal", "dense", "critical", "species", "browse", "recommend", "combination", "option", "suggestion", "fantastic", "specialty", "digestion", "encounter", "gallery", "chamber", "hooked", "physical", "viewer", "interact", "recognizable", "eternal", "disrupt", "portray", "intense", "boredom", "pursue", "series", "fame", "household", "agent", "fantasy", "franchise", "venture", "accent", "overall", "immune", "symptom", "mild", "vomit", "severe", "tolerance", "injection"

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
