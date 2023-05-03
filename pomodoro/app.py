# after i heva practiced a bit What Do I Want to make 
    # ? user chose or add it's own sound if the user didn't chose one there is the deafult DONE 
    # ? user chose how long the pomodoro times will take 
    # ? user chose how long the short braek and long one would take 
    # ? once every secion ended the user hear the shosen sound 
    # ? user see what type of secion [pomodoro, short break, long break]
    # ? user can see the clock, how much time left sor the next secion 
    # ? and a slider that have a percentage calculates the progress of the secion 
        # TODO : THAT IS ALL :)

import datetime

from termcolor import colored

from helpers import play_sound, move_to_start, clear_line, formate

import time

import sys

import time 

from rich.progress import track

chosen_sound = None

SOUND = ['suii.mp3', 'twitch.mp3', 'rock.mp3']

def main():
    while True:
        try:
            pomodoro = int(input("> Pomodoro Time : "))
            time_break = int(input("> Short Break : "))
            break
        except ValueError:
            print(colored("Write A Number Not A String You Morone", 'red'))


    chose_add = input("> Chose A Notification Sound Or Add One \n  CHOSE OR ADD OR NOTHING > ").upper()

    while True:
        if chose_add == 'CHOSE':

            for i in range(len(SOUND)):
                print(f"{i + 1} : {SOUND[i]}")

            # ! i'll come back soon to it 
            sound = int(input("Chose > ")) - 1
            chosen_sound = SOUND[sound]

            play_sound(chosen_sound)
            print(colored("> Done", 'green'))
            break

        elif chose_add == 'ADD':
            print("Downlad The Sound First And Give It's Name")
            name = input("Name > ") + '.mp3'
            SOUND.append(name)

            chosen_sound = name

            # palying the sound 
            # ! there is a bug here and i dont't know where it came from 
            try: 
                play_sound(chosen_sound)
                print(colored("Done", "green", "on_white"))
                break
            except ValueError:
                print(colored("Sound Name Not Found Try Again", "red"))

        elif chose_add == 'NOTHING':
            chosen_sound = SOUND[1]
            break


    



if __name__ == '__main__':
    main()


# for n in track(range(20), description="Processing..."):
#     # ! n here represent seconds 
#     time.sleep(n * 0.1)
