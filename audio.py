#from gtts import gTTS
#from playsound import playsound
#from googletrans import Translator
#import os
#
#Languages = ["English", "Tamil", "Malayalam", "Telugu", "Kannada", "Hindi"]
#
#texts_in_english = ["person_name_saved_as"]
#
#lang = ['en', 'ta', 'ml', 'te', 'kn', 'hi']
#
#def translate_to_language(text, dest_lang):
#    translator = Translator()
#    translated_text = translator.translate(text, src='en', dest=dest_lang)
#    return translated_text.text
#
#base_audio_path = "/home/rock/Desktop/Hearsight/audios/"
#
#for language_code in lang:
#    language_folder = f"{Languages[lang.index(language_code)]}_audio"
#    language_path = os.path.join(base_audio_path, language_folder)
#
#    if not os.path.exists(language_path):
#        os.makedirs(language_path)
#
#    for text in texts_in_english:
#        english_text = text.replace("_", " ")
#        translated_text = translate_to_language(english_text, language_code)
#
#        obj = gTTS(text=translated_text, lang=language_code, slow=False)
#
#        folder_name = os.path.join(language_path, f"{text}.mp3")
#        obj.save(folder_name)
#
#        print(f"Created: {folder_name}")

        # Play the audio (optional)
#        playsound(folder_name)


from gtts import gTTS
import playsound

# Define the text you want to convert into speech 0 5 4 2 1 3
text_1 = "say your language"
text_2 = "अपनी भाषा कहो"
text_3 = "ನಿನ್ನ ಭಾಷೆ ಹೇಳು"
text_4 = "നിങ്ങളുടെ ഭാഷ പറയൂ"
text_5 = "உங்கள் மொழியை சொல்லுங்கள்"
text_6 = "మీ భాష చెప్పండి"
#text_7 = "వ్యక్తి ముఖం విజయవంతంగా తీసివేయబడింది"

#                0        1            2          3         4         5
Languages = ["English", "Tamil", "Malayalam", "Telugu", "Kannada", "Hindi"]
langs = ['en', 'ta', 'ml', 'te', 'kn', 'hi']

index_1 = 0
index_2 = 5
index_3 = 4
index_4 = 2
index_5 = 1
index_6 = 3

# Create a gTTS object with the text and language specification
tts_1 = gTTS(text_1, lang= langs[index_1])
tts_2 = gTTS(text_2, lang= langs[index_2])
tts_3 = gTTS(text_3, lang= langs[index_3])
tts_4 = gTTS(text_4, lang= langs[index_4])
tts_5 = gTTS(text_5, lang= langs[index_5])
tts_6 = gTTS(text_6, lang= langs[index_6])
#tts_7 = gTTS(text_7, lang= langs[index])

filename_1 = "say_your_language"
filename_2 = "say_your_language"
filename_3 = "say_your_language"
filename_4 = "say_your_language"
filename_5 = "say_your_language"
filename_6 = "say_your_language"
#filename_7 = "now_press_confirm_button_to_delete_this_persons_face"


# Save the generated speech as an audio file
tts_1.save(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_1]}_audio/{filename_1}.mp3")
playsound.playsound(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_1]}_audio/{filename_1}.mp3")
tts_2.save(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_2]}_audio/{filename_2}.mp3")
playsound.playsound(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_2]}_audio/{filename_2}.mp3")
tts_3.save(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_3]}_audio/{filename_3}.mp3")
playsound.playsound(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_3]}_audio/{filename_3}.mp3")
tts_4.save(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_4]}_audio/{filename_4}.mp3")
playsound.playsound(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_4]}_audio/{filename_4}.mp3")
tts_5.save(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_5]}_audio/{filename_5}.mp3")
playsound.playsound(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_5]}_audio/{filename_5}.mp3")
tts_6.save(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_6]}_audio/{filename_6}.mp3")
playsound.playsound(f"/home/rock/Desktop/Hearsight/audios/{Languages[index_6]}_audio/{filename_6}.mp3")
#tts_7.save(f"/home/rock/Desktop/Hearsight/audios/{Languages[index]}_audio/{filename_7}.mp3")
## Play the generated audio file
#playsound.playsound(f"/home/rock/Desktop/Hearsight/audios/{Languages[index]}_audio/{filename_7}.mp3")



#online_audios = "/home/rock/Desktop/Hearsight/English/online_features/"

#main_audio_dir = "/home/rock/Desktop/Hearsight/audios/"


#face_not_registered_change_your_location_and_try_again_with_proper_lighting
#Successfully added face  
#total face
#Face not recognized
#unknown face
#no face to remove
#Successfully removed face


#person's face not registered change your location and try again with proper lighting
#Successfully added person's face  
#total person's faces
#person's Face not recognized
#unknown person's face
#no person's faces to remove
#Successfully removed person's face