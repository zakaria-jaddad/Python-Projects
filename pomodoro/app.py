import datetime

from termcolor import colored

from helpers import play_sound, move_to_start, clear_line, formate

import time

import sys

# play_sound('suii.mp3')

print(colored('worked', 'green', 'on_grey'))

    # TODO : Just for knowing the bass of this i'll make first a stopwatch timer 
seconds = 0
minutes = 0
hours = 0

while True:

    move_to_start()

    # clear_line()

    sys.stdout.write(formate(hours, minutes, seconds))
    sys.stdout.flush()

    time.sleep(1)

    # * seconds == 60 it means 1 minute 

    if seconds == 60:

        seconds = -1
        # add one minute 
        minutes  += 1

        # * hour
        if minutes == 60:
            hours += 1
            minutes = 0

    # * incremant seconds in every iteration 
    seconds += 1
