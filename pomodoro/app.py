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

    else:
        chosen_sound = SOUND[1]


    # * after all the promodoro will start here 
    while True:
        # * Working 
        if SECION_COUNTER % 2 != 0:
            print(colored("Work Time !", 'cyan'))

            for n in track(range(30), description="Work..."):
                time.sleep(1)

        # * Short Break
        elif SECION_COUNTER % 2 == 0 and SECION_COUNTER % 8 != 0:
            print(colored("Short Break", 'red'))

            for n in track(range(30), description="Break..."):
                time.sleep(1)

        # * Long Break 
        else:
            print(colored("Long Break", 'magenta')) 

            for n in track(range(15), description="Nap..."):
                time.sleep(1)


        play_sound(chosen_sound)
        SECION_COUNTER +=1



    



if __name__ == '__main__':
    main()


# for n in track(range(20), description="Processing..."):
#     # ! n here represent seconds 
#     time.sleep(n * 0.1)


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