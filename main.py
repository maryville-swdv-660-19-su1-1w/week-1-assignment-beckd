import collections as c
from random import *

def inputs():
    noun1 = input("Give us a noun: ")
    verb = input("Now a verb: ")
    adjective = input("And an adjective: ")
    noun2 = input("One more noun please: ")
    randomString = input("How about a random string of characters: ")
    noun3 = input("One more noun for the road: ")
    return noun1, verb, adjective, noun2, randomString, noun3

def intro():
    print("Welcome to Madlibs!")
    print("We'll take come inputs from you and return a funny story!")
    print("Let's get started!")

def main():
    intro()
    inputs_value = inputs()
    noun1 = inputs_value[0]
    verb = inputs_value[1]
    adjective = inputs_value[2]
    noun2 = inputs_value[3]
    randomString = inputs_value[4]
    noun3 = inputs_value[5]
    randomNumber = randrange(2, 6)
    randomNumber2 = randrange(2, 6)
    count_items = c.Counter(randomString)
    
    print()
    print("Thanks for the inputs! Now onto our story!")
    print()
    print("A guy walks into a bar with {} {}s.".format(randomNumber, noun1))
    print()
    print("Bartender asks, 'What you doing will all those {} {}s?".format(adjective, noun1))
    print()
    print("Guy says, I'll tell you if you can {} me how many of each {} is in my password {}.".format(verb, noun2, randomString))
    print()
    print("Bartend says, 'That's easy...'")
    for i in count_items:
        print('{} {}'.format(count_items[i], i))
    print()
    print("The guy says, 'That's amazing! How did you do that?'")
    print()
    print("And the bartender replies, 'I'll tell your for {} {}s!'".format(randomNumber2, noun3))
          
main()
    