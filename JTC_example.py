#   This script is to demonstrate the process of adding sound to a python program.
#   Pygame will be utilized and therefore must be installed.
#   Trenton Rice
#   Date created:       20200219
#   Last Modified on:   20200223
#   Version:            B.1
#   See github.com/TrentonR/JTC_300_Technical_Manual for version history and rev information

import pygame
import pygame.freetype
import time
#import pdb
#pdb.set_trace()
pygame.mixer.init()
pygame.freetype.init()
pygame.init()

now_play_disp=pygame.display.set_mode((400,40))
pygame.display.set_caption('TR Media Player')
bkgd=(0,0,200)

text_type=pygame.freetype.Font(None, 15)
sound_files = ['whistle_train4.mp3','air_raid.wav',
               'Ship_Bell.wav']
i=0
while i<len(sound_files):
    current_sound = sound_files[i]
    pygame.mixer.music.load(current_sound)
    play_str='Now Playing:   '+current_sound
    now_play_disp.fill((bkgd))
    text_type.render_to(now_play_disp,(5,15),play_str,(255,255,255),(bkgd),1)
    pygame.display.update()
    
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == 1:
        time.sleep(0.5)
        
    time.sleep(1)
    i=i+1
now_play_disp.fill((bkgd))
time.sleep(0.5)
text_type.render_to(now_play_disp,(5,15),'Playlist ended...Goodbye',(255,255,255),(bkgd),1)

time.sleep(10)
