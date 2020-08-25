#!/usr/bin/python3
import argparse
import json
import random
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='A string-generator of creatures-encounters.')
    parser.add_argument('range', metavar='N', type=int,
                        help='Number of fluffies to generate.')
    return parser.parse_args()

class TermColors:
    '''
    Helper class to generate terminal control sequences.
    '''
    @staticmethod
    def rgb(hh):
        '''HTML color to terminal escape sequence'''
        assert(hh[0] == '#' and len(hh) == 7)
        rr = int(hh[1:3], 16)
        gg = int(hh[3:5], 16)
        bb = int(hh[5:7], 16)
        return f'\x1b[38;2;{rr};{gg};{bb}m'
    reset = '\x1b[0m' # reset to terminal defaults

def colorize(color):
    '''
    Convert a tuple (color, string) to a terminal-colorized string.
    '''
    return T.rgb(color[0]) + color[1] + T.reset

args = parse_args()
T = TermColors()

f = open("lists.json")
data = json.load(f)

states = data["states"]
colors = data["colors"]
creatures = data["creatures"]
at_actions = data["at_actions"]
to_actions = data["to_actions"]
on_actions = data["on_actions"]
with_actions = data["with_actions"]
towards_actions = data["towards_actions"]
plain_actions = data["plain_actions"]
in_actions = data["in_actions"]
after_actions = data["after_actions"]
from_actions = data["from_actions"]
about_actions = data["about_actions"]
for_actions = data["for_actions"]
of_actions = data["of_actions"]
whisper_stuff = data["whisper_stuff"]
throwing_stuff = data["throwing_stuff"]
talking_stuff = data["talking_stuff"]
sharing_stuff = data["sharing_stuff"]
music_genres = data["music_genres"]
tv_series = data["tv_series"]

f.close()

actions_list = [whisper_stuff, talking_stuff, throwing_stuff, sharing_stuff, to_actions, on_actions, with_actions, towards_actions,
                at_actions, in_actions, after_actions, from_actions, about_actions, for_actions, of_actions, plain_actions]
actions_path = ["whispering", "talking", "throwing", "sharing", "to_actions", "on_actions", "with_actions", "towards_actions",
                "at_actions", "in_actions", "after_actions", "from_actions", "about_actions", "for_actions", "of_actions", "plain_actions"]

total_actions = 0
actions_weighted = []

for action in actions_list:
    total_actions += len(action)

for action in actions_list:
    actions_weighted.append(len(action)/total_actions)

for fluff in range(args.range):
    states_choice0 = random.choice(states)
    states_choice1 = random.choice(states)
    colors_choice0 = colorize(random.choice(colors))
    colors_choice1 = colorize(random.choice(colors))
    creatures_choice0 = random.choice(creatures)
    creatures_choice1 = random.choice(creatures)

    action_path = random.choices(actions_path,actions_weighted)[0]

    if states_choice0[0] in ["a", "e", "i", "o", "u"]:
        prefix0 = "An "
    else:
        prefix0 = "A "

    if states_choice1[0] in ["a", "e", "i", "o", "u"]:
        prefix1 = "an "
    else:
        prefix1 = "a "

    fixed_path = prefix0 + states_choice0 + " " + colors_choice0 + " " + creatures_choice0 + " and " + \
                 prefix1 + states_choice1 + " " + colors_choice1 + " " + creatures_choice1 + " are "

    if action_path == "whispering":
        whisper_choice = random.choice(whisper_stuff)
        print(fixed_path + "whispering " + whisper_choice + " to you!")
    elif action_path == "talking": 
        talking_subject = random.choice(talking_stuff)
        if talking_subject not in ["music", "tv_series", "elephant in the room"]:
            print(fixed_path + "talking about " + talking_subject + " with you!")
        elif talking_subject == "music":
            genre = random.choice(music_genres)
            print(fixed_path + "talking about " + genre + " music with you!")
        elif talking_subject == "tv_series":
            series = random.choice(tv_series)
            print(fixed_path + "talking about " + series + " with you!")
        elif talking_subject == "elephant in the room":
            colors_choice2 = colorize(random.choice(colors))
            print(fixed_path + "talking about the " + colors_choice2 + " elephant in the room with you!")

    elif action_path == "throwing":
        throwing_object = random.choice(throwing_stuff)
        if throwing_object != "blobs":
            print(fixed_path + "throwing " + throwing_object + " at you!")
        else:
            colors_choice2 = colorize(random.choice(colors))
            print(fixed_path + "throwing " + colors_choice2 + " blobs at you!")
    elif action_path == "sharing":
        sharing_object = random.choice(sharing_stuff)
        print(fixed_path + "sharing " + sharing_object + " with you!")
    elif action_path == "to_actions":
        to_action = random.choice(to_actions)
        print(fixed_path + to_action + " to you!")
    elif action_path == "on_actions":
        on_action = random.choice(on_actions)
        print(fixed_path + on_action + " on you!")
    elif action_path == "with_actions":
        with_action = random.choice(with_actions)
        print(fixed_path + with_action + " with you!")
    elif action_path == "towards_actions":
        towards_action = random.choice(towards_actions)
        print(fixed_path + towards_action + " towards you!")
    elif action_path == "at_actions":
        at_action = random.choice(at_actions)
        print(fixed_path + at_action + " at you!")
    elif action_path == "in_actions":
        in_action = random.choice(in_actions)
        print(fixed_path + in_action + " in you!")
    elif action_path == "after_actions":
        after_action = random.choice(after_actions)
        print(fixed_path + after_action + " after you!")
    elif action_path == "from_actions":
        from_action = random.choice(from_actions)
        print(fixed_path + from_action + " from you!")
    elif action_path == "about_actions":
        about_action = random.choice(about_actions)
        print(fixed_path + about_action + " about you!")
    elif action_path == "for_actions":
        for_action = random.choice(for_actions)
        print(fixed_path + for_action + " for you!")
    elif action_path == "of_actions":
        of_action = random.choice(of_actions)
        print(fixed_path + of_action + " of you!")
    elif action_path == "plain_actions":
        plain_action = random.choice(plain_actions)
        print(fixed_path + plain_action + " you!")
