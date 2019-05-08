# SWDV 660 Applied DevOps - Week 1 Assignment: Package Managed Products

### **!!WARNING: This program was built and tested on a Mac, no testing was done on a PC!! (don't own one)**

## **Executable File: MADLIB**

Project: Compile a working program via pipenv and pyinstaller

For my project I created a simple Madlibs style game. The user inputs various nouns, verbs, and strings.
Then the program outputs as simple story using the inputs given.

## Packages Used

I used **Collections** and **Random** as the two required dependencies for the program to run.

## What it Does 

When the user opens the executable file **Madlib** they are asked to put in several nouns, verbs, adjectives, and a random string
of characters. Once all the inputs are given, the program puts those items into the story and prints is out.

- The **Random** library package is used in the story to generate a random int used in the story. 

How I added them:

To the main file:
```
import collections as c 
```
Installing the package:
```
pip install collections
```
Added to the Pipfile:
```
pipenv install collection
```
- The **Collections** library package is used at a specific part of the story to count items.

How I added them:

To the main file:
```
from random import *
```
Installing the package:
```
pip install random
```
Added to the Pipfile:
```
pipenv install random
```

## What the program was built on

Program Info:
- Python 3.7.1
- Pyinstaller 3.4
- Pipenv 2018.11.26

Computer Info:
- macOS Mojave version 10.14.3

