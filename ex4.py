import argparse
import random

#1. Getting help with –help or -h.
#Done by argparse

#2. At least three arguments that are flags, meaning they don’t take an extra argument but simply putting them on the command line turns something on.
def rando(string):
	randomOutput = ""
	for char in string:
		flip = random.randint(0, 1)
		if flip == 0:
			char = char.upper()
		else:
			char = char.lower()
		randomOutput += char
	return randomOutput

def leet(string):
	leetOutput = ""
	for char in string:
		if char.lower() == "o":
			char = str(0)
		if char.lower() == "e":
			char = str(3)
		leetOutput += char
	return leetOutput

def allcaps(string):
	return string.upper()

#3. At least three arguments that are options, meaning they do take an argument and set a variable in your script to that option.
def newOutput(string):
	return string

#4. Additional “positional” arguments, which are a list of files at the end of all the – style arguments and can handle Terminal wildcards like */.txt.

parser = argparse.ArgumentParser(description='Modify some text')
parser.add_argument('--random', dest='random', action='store_true', default=False, help='randomly capitalize the output')
parser.add_argument('--leet', dest='leet',action='store_true', default=False, help='Turn the output into l33t hack3r sp3ak')
parser.add_argument('--allcaps', dest='allcaps',action='store_true', default=False, help='SHOUT THE OUTPUT')
parser.add_argument('--customoutput', action='store', default="Hack the planet, Bro!", help='Use your own string as input')

args = parser.parse_args()

output = args.customoutput

if args.random:
	output = rando(output)
if args.leet:
	output = leet(output)
if args.allcaps:
	output = allcaps(output)

print(output)
