#Level 1 is having command line options for the most basic sed usage 
#of replacing one string with another.
#Level 2 is enabling regular expressions in those command line options.
#Level 3 is implementing the sed expression format.
#example: ls –l | sed –e "s/pgcudahy/author/g"
#ls –l | sed –e "s/Jul [0 – 9][0 – 9]/DATE/g" (Hmmm, doesn't seem to work on my mac)

import argparse
import sys
import re
import fileinput

parser = argparse.ArgumentParser(description='Copy the sed utility')
parser.add_argument('file', nargs='?', default=sys.stdin, 
					type=argparse.FileType('r'), 
					help="file(s) to process (in quotes), default is stdin")
parser.add_argument('-e', action="store", dest="pattern", help="regex to apply")
args = parser.parse_args()


#Strategy: take the s/X/Y/g and decode into X and Y
def decodeSearch(pattern):
    if pattern[0] == "s":
        return (pattern.split('/')[1:3])

searchPattern, replacementPattern = decodeSearch(args.pattern)

searchPattern = re.compile(searchPattern)
#This has taken too long already
#Later may implement: g = replace all, n = replace nth occurance, I = ignore case
for line in args.file:
    print(re.sub(searchPattern, replacementPattern, line),end='')
