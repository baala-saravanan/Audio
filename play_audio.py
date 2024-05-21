from pydub import AudioSegment
from config import *
import vlc
import time
import gpio as GPIO
import os

vlc_instance = vlc.Instance()

GPIO.setup(450, GPIO.IN)
GPIO.setup(421, GPIO.IN)
GPIO.setup(447, GPIO.IN)
GPIO.setup(448, GPIO.IN)

class GTTSA:
    def get_audio_duration(self, filename):
        audio = AudioSegment.from_file(filename)
        duration_in_seconds = len(audio) / 1000  # Convert milliseconds to seconds
        return duration_in_seconds
    
    def play_machine_audio(self, voice, speed = 1.4):
        with open(LANG_FILE,'r') as file:
            language = file.read()      
        if language == "":
            language = "English"
            with open(LANG_FILE,'w') as file:
                file.write(language)
                
        MACHINE_VOICE_DIR = f"/home/rock/Desktop/Hearsight/audios/{language}_audio/"
        
        try:
            os.path.exists(MACHINE_VOICE_DIR)
            print(voice)
            filename = os.path.join(MACHINE_VOICE_DIR, voice)
            media = vlc.MediaPlayer(filename)
            media.play()
            media.set_rate(speed)  # Set the playback speed
            duration = self.get_audio_duration(filename)
            time.sleep(float(duration) / speed)  # Adjust sleep time for playback speed
            media.stop()
            media.release()
        except Exception as e:
            print(f"Audio :{voice} not found")
            pass
    
    def play_time(self,voice, speed = 1.4):
        with open(LANG_FILE,'r') as file:
            language = file.read()
        
        if language == "":
            language = "English"
            with open(LANG_FILE,'w') as file:
                file.write(language)
                
        MACHINE_VOICE_DIR = f"/home/rock/Desktop/Hearsight/audios/{language}_audio/"
        
        try:
            os.path.exists(MACHINE_VOICE_DIR)
            print(voice)
            filename = os.path.join(MACHINE_VOICE_DIR, voice)
            media = vlc.MediaPlayer(filename)
            media.play()
            media.set_rate(speed)  # Set the playback speed
            duration = self.get_audio_duration(filename)
            time.sleep((int(duration)/speed))  # Adjust sleep time for playback speed
            media.stop()
            media.release()
        except Exception as e:
            print(f"Error : {e}")
            pass
        
#        with open(LANG_FILE,'r') as file:
#            language = file.read()
#            
#        if language == "":
#            language = "English"
#            with open(LANG_FILE,'w') as file:
#                file.write(language)
#            
#        MACHINE_VOICE_DIR = f"/home/rock/Desktop/Hearsight/audios/{language}_audio/"
#        filename = os.path.join(MACHINE_VOICE_DIR, voice)        
#        vlc_instance = vlc.Instance('--no-xlib')
#        player = vlc_instance.media_player_new()
#        media = vlc_instance.media_new(filename)
#        player.set_media(media)
#        player.set_rate(playback_rate)
#        player.play()
#        player_event_manager = player.event_manager()
#        player_event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, lambda x: player.stop())
#        
#        while True:
#            state = player.get_state()
#            if state == vlc.State.Ended:
#                break
#            
#        player.release()
#        vlc_instance.release()
        
    def play_audio_file(self, voice, playback_rate = 1.1):
        
        with open(LANG_FILE,'r') as file:
            language = file.read()
            
        if language == "":
            language = "English"
            with open(LANG_FILE,'w') as file:
                file.write(language)
                
                
        MACHINE_VOICE_DIR = f"/home/rock/Desktop/Hearsight/audios/{language}_audio/"
        filename = os.path.join(MACHINE_VOICE_DIR, voice) 
        try:
            player = vlc_instance.media_player_new()  # Use the existing instance
            media = vlc_instance.media_new(filename)
            player.set_media(media)
            player.play()
            player.set_rate(playback_rate)
            paused = False
            rewind_pressed = False
            fast_forward_pressed = False
            
            duration = self.get_audio_duration(filename)
            print("Audio duration:", duration, "seconds")
            
            while True:  # Loop the audio playback until the exit button is pressed
                state = player.get_state()
                if state == vlc.State.Ended:  # Stop playback when the audio ends
                    player.stop()
                    break
                if GPIO.input(447):
                    if not paused:
                        player.set_pause(1)
                        paused = True
                    else:
                        player.set_pause(0)
                        paused = False
                    time.sleep(0.5)  # Debounce button press

                if GPIO.input(448):
                    player.stop()
                    self.play_machine_audio("feature_exited.mp3")
                    break

                if GPIO.input(450):
                    if not fast_forward_pressed:
                        current_time = player.get_time()
                        new_time = current_time + 1000  # Fast forward by 1 seconds
                        player.set_time(new_time)
                        fast_forward_pressed = True
                else:
                    fast_forward_pressed = False

                if GPIO.input(421):
                    if not rewind_pressed:
                        current_time = player.get_time()
                        new_time = current_time - 1000  # Rewind by 1 seconds
                        if new_time < 0:
                            new_time = 0
                        player.set_time(new_time)
                        rewind_pressed = True
                else:
                    rewind_pressed = False

                time.sleep(0.2)  # Introduce a delay

        except Exception as e:
            print("An error occurred:", e)
            
