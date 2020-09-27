"""
A simple meditation script

Notes for bugs:
    Everything works so far! No bugs!!
"""


import time
from rich import print
from pygame import mixer
from datetime import date, datetime
import sys


def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue

        return inp


def music():
    """
    Music for meditations. For now its "It's Ok - Forrest.
    """
    # * How many times the user wants to repeat the music
    repeat_music = ask_for(
        '\nHow many times would you like to repeat the currently playing music?: ', _type=int)

    # * While the input above ^ is over 10, repeat the prompt. Else play the music x amount of times.
    not_music = True
    while not_music:
        # * Repeat_music is over 10
        if repeat_music >= 11:
            print('You cant repeat the music over 10 times.')
            repeat_music = ask_for(
                '\nHow many times would you like to repeat the currently playing music?: ', _type=int)
        # * Got a result thats fine, so break out of loop.
        else:
            not_music = False

    # * Then for _ in range of how many times the user wants to play the music, it plays.
    # * e.g repeat_music = 3, so this code below loops over itself 3 times.
    for _ in range(repeat_music):
        mixer.init()
        mixer.music.load("/Users/justinbuan/Downloads/It's Okay (Outro).mp3")
        mixer.music.play()


def welcome_message(meditation_name=str):
    """
    A welcome mesage that tells the user what meditation they picked
    and when it will start.

    Args:
        meditation_name (str, optional): Meditation name. (e.g Equal Breathing) Defaults to str.
    """
    # * Welcomes the user to the meditation
    print('\nHi! [bold white]Welcome[/] to the meditation.')
    time.sleep(2.5)
    # * Gives the meditation name and when it will start.
    print(
        f'This is the [bold white]{meditation_name}[/] meditation. It will [bold white]start[/] in 10 seconds.')
    time.sleep(10)


class Meditations():
    """
    All of the meditations used in this script.
    """

    def box(self):
        welcome_message('Box Breathing')
        # Loops 8 times to get a full minute.
        for _ in range(8):
            # * Breathe in
            print('\n------------------------------')
            print('[blue]Breathe in[/]...')
            time.sleep(4)

            # * Hold
            print('\n[blue]Hold[/]')
            time.sleep(4)

            # * Breathe Out
            print('\n[Bold White]Breathe out[/]...')
            time.sleep(4)
            print('------------------------------')

    def calm_down(self):
        welcome_message('Equal Breathing')
        # Loops 8 times to get a minute or slightly over a minute
        for _ in range(8):
            # * Breathe in
            print('\n------------------------------')
            print('[blue]Breathe in for 4[/]...')
            time.sleep(4)

            # * Breathe out
            print('\n[bold white]Breathe out for 4...[/]')
            time.sleep(4)
            print('------------------------------')

    def deep_relax(self):
        welcome_message('Relax Deeply')
        # Loops over 3 times to get a minute
        for _ in range(3):
            # * Breathe in
            print('\n------------------------------')
            print('[blue]Breathe in for 4...[/]')
            time.sleep(4)

            # * Hold
            print('\nHold for 7...')
            time.sleep(7)

            # * Breathe out
            print('\n[bold white]Exhale for 8...[/]')
            time.sleep(8)
            print('------------------------------')

    def extended_exhale(self):
        welcome_message('Extended Exhale')
        # Loops over itself 6 times to get a full minute
        for _ in range(6):
            # * Breathe in
            print('\n------------------------------')
            print('[blue]Breathe in for 4[/]...')
            time.sleep(4)

            # * Breathe out
            print('\n[bold white]Breathe out for 6...[/]')
            time.sleep(6)
            print('------------------------------')

    def gratitude(self):
        """
        Creates a text file based off of 3 things the user is grateful for.
        It also records a happiness scale ( 1 - 10 ) and the current date and time.
        """
        # Informational stuff
        print('\nWelcome to the gratitude part of your meditation. Below, name your text file, and then name 3 things you are grateful for.')

        # * Filename
        filename = ask_for(
            '\nWhat would you like to call your text file? ( Dont include file extension ): ', _type=str)
        # * Adds .txt to end of whatever the user calls their file
        filename = filename + '.txt'

        # * Opens the file
        with open(filename, "x") as f:
            counter = 0
            # * Kinda bad code with the counter but, the code below
            # * loops over itself 3 times to get input out of the user.
            for _ in range(3):
                counter += 1
                print(f'\n{counter} You are [bold white]grateful[/] for:')
                f.write(f'\n {counter}. ' + ask_for('\n: ', _type=str))

            # * Happiness scale
            print(
                '\nOn a scale of 1-10 how [bold white]happy[/] are you right now?')
            happiness_scale = ask_for('\n: ', _type=float)

            # * Writes the happiness scale to the file and the current date and time.
            f.write(f"\nHappiness scale ( 1 - 10 ): {happiness_scale}")
            f.write(f"\nToday's date is: {datetime.now()} ")


m = Meditations()

if __name__ == "__main__":
    # * Lists all the meditations and starts the music
    def start():
        """
        Startup of script. Plays music and lists all meditations.
        """
        music()
        print('\nHi! There are 4 [bold white]options[/].')

        # Extended exhale
        print('\n[bold white]Calming Down[/] ( 1 )')
        print('[blue]Extended Exhale[/]')

        # Equal Breathing
        print('\n[bold white]Clearing the Mind[/] ( 2 )')
        print('[blue]Equal Breathing[/]')

        # Relax Deeply
        print('\n[bold white]Relax Deeply[/] ( 3 )')
        print('[blue]4 - 7 - 8 Breathing[/]')

        # Box breathing
        print('\n[bold white]Relieve Stress[/] ( 4 )')
        print('[blue]Box Breathing.[/]')

        # * Asking the user which meditation they want to choose.
        print('\nWhich meditation would you like to choose? ( 1 - 4 )')
        print(
            'Please keep in mind these will all run for around [bold white]1 minute to 1.5 minutes[/].')
        which_meditation = ask_for('\n: ', _type=int)

        def repeat_meditation():
            """
            Asks the user if they want to repeat the script.
            """
            print('\nWould you like to [blue]choose[/] another meditation?')
            repeat = ask_for('\n(y/n): ').lower()

            if repeat == 'n':
                print('\nThanks for [bold white]meditating[/]!')
                sys.exit()
            if repeat == 'y':
                start()

        # * While the input isn't 1 - 4, repeat the prompt.
        not_meditation = True
        while not_meditation:

            if which_meditation <= 4:

                if which_meditation == 1:
                    m.extended_exhale()
                    m.gratitude()
                    repeat_meditation()

                if which_meditation == 2:
                    m.calm_down()
                    m.gratitude()
                    repeat_meditation()

                if which_meditation == 3:
                    m.deep_relax()
                    m.gratitude()
                    repeat_meditation()

                if which_meditation == 4:
                    m.box()
                    m.gratitude()
                    repeat_meditation()
            else:
                which_meditation = ask_for('\n: ', _type=int)

    start()
