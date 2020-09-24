"""
A simple meditation script

Notes for bugs:
    Everything works so far! No bugs!!
"""


import time
from rich import print
from pygame import mixer


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
    repeat_music = ask_for(
        '\nHow many times would you like to repeat the currently playing music?: ', _type=int)

    not_music = True
    while not_music:
        if repeat_music >= 11:
            print('You cant repeat the music over 10 times.')
            repeat_music = ask_for(
                '\nHow many times would you like to repeat the currently playing music?: ', _type=int)
        else:
            not_music = False

    for _ in range(repeat_music):
        mixer.init()
        mixer.music.load("/Users/justinbuan/Downloads/It's Okay (Outro).mp3")
        mixer.music.play()


def welcome_message(meditation_name=str):
    print('\nHi! [bold white]Welcome[/] to the meditation.')
    time.sleep(2.5)
    print(
        f'This is the [bold white]{meditation_name}[/] meditation. It will [bold white]start[/] in 10 seconds.')
    time.sleep(10)


class Meditations():

    def box(self):
        welcome_message('Box Breathing', [4, 4])
        for _ in range(8):
            print('\n------------------------------')
            print('[blue]Breathe in[/]...')
            time.sleep(4)

            print('\n[blue]Hold[/]')
            time.sleep(4)

            print('\n[Bold White]Breathe out[/]...')
            time.sleep(4)
            print('------------------------------')

    def calm_down(self):
        welcome_message('Equal Breathing')
        for _ in range(8):
            print('\n------------------------------')
            print('[blue]Breathe in for 4[/]...')
            time.sleep(4)
            print('\n[bold white]Breathe out for 4...[/]')
            time.sleep(4)
            print('------------------------------')

    def deep_relax(self):
        welcome_message('Relax Deeply')
        for _ in range(3):
            print('\n------------------------------')
            print('[blue]Breathe in for 4...[/]')
            time.sleep(4)

            print('\nHold for 7...')
            time.sleep(7)

            print('\n[bold white]Exhale for 8...[/]')
            time.sleep(8)
            print('------------------------------')

    def extended_exhale(self):
        welcome_message('Extended Exhale')
        for _ in range(6):
            print('\n------------------------------')
            print('[blue]Breathe in for 4[/]...')
            time.sleep(4)
            print('\n[bold white]Breathe out for 6...[/]')
            time.sleep(6)
            print('------------------------------')


m = Meditations()

if __name__ == "__main__":
    def start():
        music()
        print('\nHi! There are 4 [bold white]options[/].')

        # * Extended exhale
        print('\n[bold white]Calming Down[/] ( 1 )')
        print('[blue]Extended Exhale[/]')

        print('\n[bold white]Clearing the Mind[/] ( 2 )')
        print('[blue]Equal Breathing[/]')

        print('\n[bold white]Relax Deeply[/] ( 3 )')
        print('[blue]4 - 7 - 8 Breathing[/]')

        print('\n[bold white]Relieve Stress[/]')
        print('[blue]Box Breathing.[/]')

        print('\nWhich meditation would you like to choose? ( 1 - 4 )')
        print(
            'Please keep in mind these will all run for around [bold white]1 minute to 1.5 minutes[/].')
        which_meditation = ask_for('\n: ', _type=int)

        def repeat_meditation():
            print('\nWould you like to [blue]choose[/] another meditation?')
            repeat = ask_for('\n(y/n): ').lower()

            if repeat == 'n':
                print('\nThanks for [bold white]meditating[/]!')
            if repeat == 'y':
                start()

        not_meditation = True
        while not_meditation:

            if which_meditation <= 4:

                if which_meditation == 1:
                    m.extended_exhale()
                    repeat_meditation()

                if which_meditation == 2:
                    m.calm_down()
                    repeat_meditation()

                if which_meditation == 3:
                    m.deep_relax()
                    repeat_meditation()

                if which_meditation == 4:
                    m.box()
                    repeat_meditation()
            else:
                which_meditation = ask_for('\n: ', _type=int)

    start()
