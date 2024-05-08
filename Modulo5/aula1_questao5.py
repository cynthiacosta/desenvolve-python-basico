import emoji

emojis = {
    ":grinning_face:": "😀",
    ":thumbs_up:": "👍",
    ":rocket:": "🚀",
    ":fire:": "🔥",
    ":face_with_tears_of_joy:": "😂",
    ":blue_heart:": "💙",
    ":sunflower:": "🌻",
    ":earth_americas:": "🌎",
    ":check_mark_button:": "✅",
    ":alarm_clock:": "⏰"
}

print("Aqui está uma lista de emojis disponíveis e seus códigos:")
for text, emj in emojis.items():
    print(f"{text}: {emj}")

frase_codificada = input("\nDigite uma frase usando os códigos de emoji acima: ")

frase_emojizada = emoji.emojize(frase_codificada, language='alias')
print("\nAqui está sua frase com emojis:")
print(frase_emojizada)