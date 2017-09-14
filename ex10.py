#Features
#Import files and concatenate together
#Sort lines
#Ignore case
#Reverse sort
#Merge without sorting
#Output to file
#
#Examples ls | sort

import argparse
import sys

parser = argparse.ArgumentParser(description='Copy the sort utility')
parser.add_argument('file', nargs='?', default=sys.stdin, 
					type=argparse.FileType('r'), 
					help="file(s) to process (in quotes), default is stdin")
parser.add_argument('-i', '--ignore-case', action="store_true", dest="ignoreCase", help="Ignore case when sorting")
parser.add_argument('-r', '--reverse', action="store_true", dest="reverse", help="Reverse sort")
parser.add_argument('-m', '--merge', action="store_true", dest="merge", help="Merge without sorting")
parser.add_argument('-o', '--output-file', action="store", dest="outFile", help="Save output to file")
args = parser.parse_args()

lines = []
keySort = str
reverseSort = False

def mergeLines(files):
	lines = []
	for line in files:
		lines.append(line)
	return files
#This seems horribly inefficient

if args.ignoreCase:
	keySort = str.lower

if args.reverse:
	reverseSort = True

def sortLines(files):
	lines = []
	for line in files:
	    lines.append(line)
	return sorted(lines, key=keySort, reverse=reverseSort)

if (args.outFile is not None) & args.merge:
	with open(args.outFile, 'w') as file:
		for item in mergeLines(args.file):
			file.write(item)
if (args.outFile is not None) & (not args.merge):
	with open(args.outFile, 'w') as file:
		for item in sortLines(args.file):
			file.write(item)
if (not args.outFile) & args.merge:
	for item in mergeLines(args.file):
		print(item, end='')
if (not args.outFile) & (not args.merge):
	for item in sortLines(args.file):
		print(item, end='')

