# this is for removing the alert evry time i use the play_sound function the trerminal 
from os import environ
import datetime
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import sys


def play_sound(title):
    pygame.init()

    pygame.mixer.music.load(title)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue


def formate(H, M, S):
    output = ""
    TIME = [H, M, S]
    # ! H could be > 9 or < 9 
    for time in TIME:
        if time < 10:
            output += f"0{time}:"
        else:
            output += f"{time}:"
        
    return output[:-1]


def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time