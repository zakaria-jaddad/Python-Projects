# this is for removing the alert evry time i use the play_sound function the trerminal 
from os import environ


import datetime

import requests

from rich.progress import track
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from termcolor import colored

import time

import sys

import json


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

    while True:

        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

        sys.stdout.write('\r')
        sys.stdout.flush()

        sys.stdout.write(current_time)


        time.sleep(1)




def tracker(timer, description):
    for n in track(range(timer * 60), description=colored(description, 'cyan')):
        time.sleep(1)


def quots():

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    while True:

        try:

            response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en", headers=headers)

            quote = response.json()["quoteText"]
            # author = response.json("quoteAuthor")

            if quote:
                return quote
        
        except json.JSONDecodeError:
            continue




