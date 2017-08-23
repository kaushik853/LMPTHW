import argparse
import glob
import re

#Load arguments. Most important are the expression to match and 
#file(s) to search
parser = argparse.ArgumentParser(description='Copy the grep utility')
parser.add_argument('pattern', help="regex to match")
parser.add_argument('file', help="file(s) to search (in quotes)")
args = parser.parse_args()

#Generate list of files to search
files = []

for file in glob.glob(args.file):
	files.append(file)
#print(files)

#Read files and search for pattern
#First compile the search pattern and initialize a list of match results
regex = re.compile(args.pattern)
matched_lines = []

#Open each file and search each line for the pattern. Append matches
#to the matched_lines list in a format similar to grep
for file in files:
	with open(file) as f:
		content = f.readlines()
		for line in content:
			#print("Searching",line,"for",args.pattern)
			match = regex.search(line)
			if match:
				matched_lines.append(file + ":" + line)

#Return list of matches
if len(matched_lines) > 0:
	for match in matched_lines:
		print(match)
else:
	print("No matches")

#Issues - the shell automatically expands wildcards in arguments so need to put
#any file patterns in quotes. eg "*.txt" instead of .txt