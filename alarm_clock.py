import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.wav"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! ☀️")

            # below is used to initialize the mixer module with default settings, mixer is the module which gives us the ability to load and play the music
            pygame.mixer.init()
            # below is used to load our sound file first 
            pygame.mixer.music.load(sound_file)
            # below is used to play the sound file
            pygame.mixer.music.play()

            # below is used to play the sound until it gets over or our program is interrupted abruptly!
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        time.sleep(1)



if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)