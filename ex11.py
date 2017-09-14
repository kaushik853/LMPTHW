import argparse
import sys

parser = argparse.ArgumentParser(description='Copy the uniq utility')
parser.add_argument('file', nargs='?', default=sys.stdin, 
					type=argparse.FileType('r'), 
					help="file(s) to process (in quotes), default is stdin")

args = parser.parse_args()

def compareLines(file):
	prevLine = ""
	for line in file:
		if line == prevLine:
			continue
		else:
			prevLine = line
			print(line, end='')

compareLines(args.file)