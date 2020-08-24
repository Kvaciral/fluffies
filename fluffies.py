#!/usr/bin/python3
import argparse
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

states = ["cuddly", "grumpy", "agitated", "shy", "bored", "boisterous", "cute", "hungry", "sleepy", "inquisitive", "scared", "playful", "clueless", "confused", "sad", "pondering", "ignorant", "cheerful", "gloomy", "ecstatic", "depressed", "judgmental", "disillusioned", "frustrated", "mad", "skeptical", "clumsy", "lithe", "assertive", "pious", "narcissistic", "timid", "megalomaniacal", "starving", "absent-minded", "chubby", "dazzling", "unkempt", "bewildered", "scrawny", "obnoxious", "ambitious", "zealous", "witty", "kind", "lazy", "scary", "intimidating", "nervous", "silly", "enigmatic", "worried", "adventurous", "old-fashioned", "adorable", "sullen", "deranged", "nerdy", "geeky", "wise", "sophisticated", "weary", "agnostic", "introverted", "affable", "bright", "shrewd", "compassionate", "conscientious", "considerate", "creative", "diplomatic", "easygoing", "fearless", "friendly", "funny", "gregarious", "modest", "inventive", "intellectual", "independent", "rebellious", "optimistic", "stubborn", "romantic", "unassuming", "mischievous", "heroic", "boastful", "arrogant", "greedy", "cowardly", "clingy", "careless", "impatient", "narrow-minded", "selfish", "cynical", "bitchy", "confrontational", "vain", "aloof", "belligerent", "pompous", "machiavellian", "sneaky", "dogmatic", "pragmatic", "resentful", "possesive", "gullibe", "naive", "finicky", "vulgar", "charming", "amiable", "sympathetic", "observant", "airheaded", "diligent", "kooky", "hilarious", "laid-back", "courageous", "snarky", "stoic", "zen", "surly"]
colors = [
    ("#5218fa", "han purple"),
    ("#990000", "crimson red"),
    ("#4682b4", "metallic blue"),
    ("#ffd300", "cyber yellow"),
    ("#ff8c00", "dark orange"),
    ("#228B22", "forest green"),
    ("#eae0c8", "pearl white"),
    ("#100C08", "smoky black"),
    ("#f5f5dc", "beige"),
    ("#f28500", "tangerine"),
    ("#8c1717", "scarlet"),
    ("#ee82ee", "violet"),
    ("#4b0082", "indigo"),
    ("#a52a2a", "brown"),
    ("#808080", "grey"),
    ("#c0c0c0", "silver"),
    ("#343434", "jet black"),
    ("#ffffff", "iridescent"),
    ("#ff00ff", "fuchsia"),
    ("#996515", "golden brown"),
    ("#ff00ff", "magenta"),
    ("#ffffff", "translucent"),
]
creatures = ["cat", "beagle", "labrador", "chihuahua", "bull", "cow", "elephant", "horse", "crocodile", "alligator", "shark", "seal", "sea lion", "walrus", "emperor penguin", "gentoo penguin", "chicken", "ostrich", "tiger", "lion", "gazelle", "hippo", "rhino", "eagle", "dove", "seagull", "cliff racer", "sparrow", "orang-utan", "chimpanzee", "gorilla", "donkey", "bear", "duck", "pig", "tyrannosaurus-rex", "brachiosaurus", "pterodactyl", "stegosaurus", "velociraptor", "zerg", "blob", "blowfish", "mackerel", "dopefish", "guppy", "wolf", "dolphin", "giant sandworm", "sheep", "mouse", "rat", "kangaroo", "octopus", "rabbit", "goat", "rattlesnake", "king cobra", "great horned owl", "elf-owl", "swan", "giraffe", "sperm whale", "humpback whale", "fin whale", "dragon", "platypus", "mammoth", "fox", "goose", "turtle", "unicorn", "phoenix", "mogwai", "gremlin", "chupacabra", "ent", "hydra", "lynx", "wyvern", "hyena", "koala", "buffalo", "crab", "cougar", "bat", "mole", "axolotl", "anteater", "elk", "deer", "moose", "dodo", "frog", "toad", "hedgehog", "emu", "wyrm", "drake", "hamster", "yeti", "jaguar", "gecko", "lemming", "lobster", "parrot", "maine coon", "weasel", "mongoose", "octopus", "panther", "hare", "turkey", "tapir", "wallaby", "wildebeest", "sasquatch", "goa'uld", "squirrel", "beaver", "silt-strider", "pokemon"]

at_actions = ["looking", "smirking", "staring", "pouncing", "yawning", "growling", "purring", "yelling", "laughing", "beaming", "belching", "sneezing", "mad", "meowing", "sighing", "shooing", "whistling", "smiling", "winking", "grinning", "blowing", "glowering", "cheering", "waving", "barking", "frowning", "aiming", "scowling", "cringing", "sniffing"]
to_actions = ["adjusting", "admitting something", "listening", "replying", "responding", "seeing", "speaking", "subscribing", "turning", "answering", "lying", "singing", "grunting", "bowing deeply", "delivering a pizza", "indifferent", "writing a letter", "being jerks", "being disrespectful", "handing a package", "apologizing", "objecting", "selling", "dealing some cards", "dealing some drugs", "preaching"]
on_actions = ["gaining ground", "jumping up and down", "feasting", "declaring war", "waiting", "counting", "homing in", "depending", "projecting", "imposing their will", "turning", "getting medieval"]
with_actions = ["agreeing", "disagreeing", "argueing", "colliding", "fighting", "quarreling", "meeting", "toying", "philosophizing", "reminiscing", "upset", "dancing", "dining", "playing a game of tic-tac-toe", "smoking a joint", "drinking a beer", "fed up", "weeping", "singing a song", "harvesting the land", "waging a war", "chilling", "laughing", "mesmerized", "making a deal", "collaborating", "associating", "making peace", "partying", "playing a game of poker"]
towards_actions = ["walking", "running", "flying", "swimming", "bouncing", "rolling", "wombling", "air-floating", "galloping", "sailing", "jet skiing", "paragliding", "shuffling"]
plain_actions = ["ignoring", "killing", "mocking", "patronizing", "hunting", "hugging", "insulting", "praising", "suing", "begrudging", "scrutinizing", "discussing", "mugging", "trolling", "watching", "berating", "punishing", "confronting", "representing", "not amused by", "blackmailing", "immortalizing", "arresting", "curing", "incarcerating", "reviewing", "ratifying", "judging", "impeaching", "buying", "selling", "gaslighting", "zapping", "trash-talking", "poking", "worshipping", "teaching", "mindreading", "spoiling", "neglecting", "firing", "serving"]
in_actions = ["disappointed", "having faith"]
after_actions = ["looking", "coming"]
from_actions = ["running away", "turning away", "getting their money's worth", "taking no bullshit", "slowly backing away", "hiding", "taking your sanity"]
about_actions = ["argueing", "caring", "concerned", "dreaming", "forgetting", "hearing", "joking", "talking", "quarreling", "thinking", "worrying", "writing a book", "warning the others", "being warned"]
for_actions = ["accounting", "taking care", "paying", "preparing", "providing", "searching", "substituting", "rooting", "working", "embarrassed", "responsible", "taking the bullet"]
of_actions = ["standing in front", "making fun", "approving", "dreaming", "getting rid", "getting tired", "hearing", "being reminded", "mindful", "totally unaware", "a vivid hallucination", "taking care"]

whisper_stuff = ["profanities", "sweet nothings", "death-threats", "declarations of independence", "evil dark secrets", "the next winning lottery numbers", "what they had for breakfast", "the answer to the meaning of life", "their new year resolutions", "their prejudices", "their deepest fears", "their root passwords", "something unintelligible", "the location of Atlantis"]
throwing_stuff = ["bananas", "mud", "stones", "nuclear bombs", "twigs", "snowballs", "blobs", "lawsuits", "money", "paper airplanes", "empty cans", "facts and statistics", "ancient gods", "staplers", "the kitchen sink", "floppy disks", "sweet potatoe pies", "dart arrows", "rotten tomatoes and eggs", "ancient IBM mainframes", "magical fireballs", "shrubberies", "logical bombs", "towels", "a hula hoop"]
talking_stuff = ["the stormy weather", "social progressive politics", "rpg computer-games", "the meaning of life", "interstellar travel", "surreal stuff", "music", "science-fiction books", "wanton destruction", "world domination", "computer security", "tv_series", "bathroom hygiene", "the new world order", "tribalism", "the merits of wearing fluffy shoes", "Picard versus Kirk", "bitcoin", "boring stuff", "global warming", "eating contests", "Python", "life extension", "anthropomorphism", "Mars colonization", "their fierce opposition to WW3", "the incoming meteorite", "tabletop rpg-gaming", "the newest computer hardware", "vikings", "the end of the world", "the monster of Loch Ness", "social distancing", "vegetarianism", "the state of the economy"]
sharing_stuff = ["their hopes and dreams", "their vegetarian lunch", "a tiny run-down apartment downtown", "their miserable sorrows", "a feast fit for kings", "the spoils of war", "their expertise on the subject", "their swimming pool", "their FTL spaceship", "their server", "a joint", "their planet", "their spice melange"]

music_genres = ["rap", "classical", "bitpop", "industrial", "ebm", "hiphop", "jazz", "electronic", "ambient", "80s", "reggae", "rock", "country", "techno", "gospel", "black metal", "alternative rock", "ska", "new wave", "punk", "dubstep", "hardstyle", "happy hardcore", "rave", "symphonic metal"]
tv_series = ["Breaking Bad", "Sons of Anarchy", "The Witcher", "Game of Thrones", "Teenage Mutant Ninja Turtles", "Black Mirror", "Babylon 5", "Castlevania", "The Expanse"]

actions_list = [whisper_stuff, talking_stuff, throwing_stuff, sharing_stuff, to_actions, on_actions, with_actions, towards_actions, at_actions, in_actions, after_actions, from_actions, about_actions, for_actions, of_actions, plain_actions]
actions_path = ["whispering", "talking", "throwing", "sharing", "to_actions", "on_actions", "with_actions", "towards_actions", "at_actions", "in_actions", "after_actions", "from_actions", "about_actions", "for_actions", "of_actions", "plain_actions"]

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

    fixed_path = prefix0 + states_choice0 + " " + colors_choice0 + " " + creatures_choice0 + " and " + prefix1 + states_choice1 + " " + colors_choice1 + " " + creatures_choice1 + " are "

    if action_path == "whispering":
        whisper_choice = random.choice(whisper_stuff)
        print(fixed_path + "whispering " + whisper_choice + " to you!")
    elif action_path == "talking": 
        talking_subject = random.choice(talking_stuff)
        if talking_subject not in ["music", "tv_series"]:
            print(fixed_path + "talking about " + talking_subject + " with you!")
        elif talking_subject == "music":
            genre = random.choice(music_genres)
            print(fixed_path + "talking about " + genre + " music with you!")
        elif talking_subject == "tv_series":
            series = random.choice(tv_series)
            print(fixed_path + "talking about " + series + " with you!")
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
