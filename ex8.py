#Implement the cut tool
#The cut command takes options that set a type of delimiter 
#and then a list of fields to extract
#Examples: cut -d ':' -f 1,7 /etc/passwd 
#		   ls –l | cut –d ' ' –f 5-7
#		   who | cut -c 1-16,26-38

#Set commandline options. Default to standard input or optional file
#First option is -d which sets a 
#Second is -f for a list of fields to extract


import argparse
import sys

parser = argparse.ArgumentParser(description='Copy the cut utility')
parser.add_argument('file', nargs='?', default=sys.stdin, 
					type=argparse.FileType('r'), 
					help="file(s) to cut (in quotes), default is stdin")
parser.add_argument('-d', default='	', help="delimiter, tab is default")
parser.add_argument('-f', help="list by field position")
parser.add_argument('-c', help="list by character position")
args = parser.parse_args()

### Parse by character
#First clean number ranges into python slices. Per 'man cut':
# Number ranges consist of a number, a dash
# (`-'), and a second number and select the fields or columns from the
# first number to the second, inclusive.  Numbers or number ranges may be
# preceded by a dash, which selects all fields or columns from 1 to the
# last number.  Numbers or number ranges may be followed by a dash, which
# selects all fields or columns from the last number to the end of the
# line.


#cut() expects numbers to be indexed from 1 rather than 0, so off by one
#It took me HOURS to figure out how to unpack the list and decrement it,
#with a long detour in regex land
#The second number is INCLUSIVE which differs from python slices so don't decrement
def charCut():
	slices = args.c.split(',')
	for index, slice in enumerate(slices):
		if '-' not in slice:
			slices[index] = [int(slice) - 1, int(slice)]
		else:
			splitted=slice.split("-")
			splitted[0] = int(splitted[0]) -1 if splitted[0] !=("") else None
			splitted[1] = int(splitted[1]) if splitted[1] !=("") else None
			slices[index] = splitted
#Now run through lines and cut out slices. 
	match  = []
	for line in args.file:
		submatch = ""
		for slice in slices:
			submatch += (line[slice[0]:slice[1]]) 
		match.append(submatch.rstrip('\n'))
	return match

if args.c:
	out = charCut()
	print(*out, sep='\n')

### Parse by field
def fieldCut():
	match  = []
	slices = args.f.split(',')
	for index, slice in enumerate(slices):
		if '-' not in slice:
			slices[index] = [int(slice) - 1, int(slice)]
		else:
			splitted=slice.split("-")
			splitted[0] = int(splitted[0]) -1 if splitted[0] !=("") else None
			splitted[1] = int(splitted[1]) if splitted[1] !=("") else None
			slices[index] = splitted

	match = []
	for line in args.file:
		submatch = []
		for slice in slices:
			submatch.append(line.split(args.d)[slice[0]:slice[1]])
		submatchString = args.d.join(str(r) for v in submatch for r in v)
		match.append(submatchString.rstrip('\n'))
	return match

if args.f:
	out = fieldCut()
	print(*out, sep='\n')
