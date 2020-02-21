#   This script is to demonstrate the process of adding sound to a python program.
#   Pygame will be utilized and therefore must be installed.
#   Trenton Rice
#   Date created:       20200219
#   Last Modified on:   20200219
#   Version:            A.0
#   See github.com/TrentonR/JTC_300_Technical_Manual for version history and rev information

import pygame
import time
#import pdb
#pdb.set_trace()
pygame.mixer.init()

sound_files = ['whistle_train4.mp3','air_raid.wav','Ship_Bell.wav']
i=0
while i<len(sound_files):
    current_sound = sound_files[i]
    pygame.mixer.music.load(current_sound)
    play_str='Now Playing:   '+current_sound
    print(play_str)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == 1:
        time.sleep(0.5)
        
    time.sleep(2.5)
    i=i+1

print('Playlist ended...Goodbye.')
time.sleep(10)
quit
