# after i heva practiced a bit What Do I Want to make 
    # ? user chose or add it's own sound if the user didn't chose one there is the deafult DONE 
    # ? user chose how long the pomodoro times will take DONE 
    # ? user chose how long the short braek and long one would take DONE 
    # ? once every secion ended the user hear the shosen sound DONE
    # ? user see what type of secion [pomodoro, short break, long break] DONE
    # ? user can see the clock, how much time left sor the next secion 
    # ? and a slider that have a percentage calculates the progress of the secion DONE 
        # TODO : THAT IS ALL :)

import datetime

from termcolor import colored

from helpers import play_sound, formate, get_time, tracker, quots

import time

import sys

import warnings

import threading

import random

import os

import time 

chosen_sound = None

# * scanning the sounds dir to get audios and strore them SOUND_DIR list 

SOUND_DIR = os.listdir('/Users/zakariajaddad/Documents/GitHub/Python-Projects/pomodoro/sounds')

# * here just for adding the path for the folder and store it in SOUND 
SOUND = []
for sound in SOUND_DIR:
    sound_path_name = "./sounds/" + sound
    SOUND.append(sound_path_name)


# ? if you wonder why i used two lists it's just because one will be shown to the user and the other 
    # ? gives the path for the play_sound function 

def main():

    if len(sys.argv) < 3:
        warnings.warn("The Script Accept 3 Arguments 'Name' 'Pomodoro Timer' 'Break Timer'")
        sys.exit()

    SECION_COUNTER = 1

    try:
        POMODORO = int(sys.argv[1])
        BREAK_TIME = int(sys.argv[2])

        # ! checking if there is any negative or zero value 
        if POMODORO < 1 or BREAK_TIME < 1:
            print(colored("Please Write A Positive Number Try Again...", 'red'))            
            sys.exit()
    except ValueError:
        print(colored("Write A Number Not A String You Morone", 'red'))
        sys.exit()

    foo = input("> Press 'E' For Settings ").upper()

    if foo == 'E':
        chose_add = input("> Chose A Notification Sound Or Add One \n  CHOSE OR ADD ").upper()

        while True:
            if chose_add == 'CHOSE':

                for i in range(len(SOUND_DIR)):
                    print(f"{i + 1} : {SOUND_DIR[i]}")

                # ! i'll come back soon to it 
                sound = int(input("Chose > ")) - 1
                chosen_sound = SOUND[sound]

                play_sound(chosen_sound)
                print(colored("> Done", 'green'))
                break

            elif chose_add == 'ADD':
                print("Downlad The Sound First And Put In 'Sounds folder' To Chose it ")

    else:
        chosen_sound = SOUND[1]


    # * after all the promodoro will start here 
    while True:
        # * Working 
        if SECION_COUNTER % 2 != 0:
            print(colored("Work Time !", 'cyan'))

            tracker(POMODORO, "Work...")

        # * Short Break
        elif SECION_COUNTER % 2 == 0 and SECION_COUNTER % 8 != 0:
            print(colored("Short Break", 'red'))

            tracker(BREAK_TIME, "Break...")

        # * Long Break 
        else:
            print(colored('Congrats 🤍 You Made It Nice Work, This Quote Is For You', 'white', 'on_cyan', ['bold']))
            print(quots())
            play_sound('./sounds/congrats/congrats_1.mp3')

            print(colored("Long Break", 'magenta')) 

            tracker(1, TODO_IN_BREAK_TIME[random.randint(0, len(TODO_IN_BREAK_TIME) - 1)])


        play_sound(chosen_sound)
        os.system("clear||cls")
        SECION_COUNTER +=1



if __name__ == '__main__':
    TODO_IN_BREAK_TIME = [
        "Take A Nap...", 
        "Read Book...", 
        "Talk With Family...", 
        "Do Some Pushups...", 
        "Read Quran...", 
        "Watch Youtube...", 
        "Drink Water...", 
        "Meditate..."
    ]

    main()

# ! os we have 4 promodomos to get the long break and evry time a promodomo section ends a short break starts 
#   ! so this is like this {
        # ! 1 : work, 
        # ! 2 : short break     
        # ! 3 : work, 
        # ! 4 : short break  
        # ! 5 : work, 
        # ! 6 : short break     
        # ! 7 : work, 
        # ! 8 : long break     
# ! }
    # ! as you can see in this list the section follow allong like this 
        # ! it's just a simple counter wiht some conditions and you can goo wiht it 