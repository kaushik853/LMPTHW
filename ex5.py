import argparse
import sys

parser = argparse.ArgumentParser(description='Copy the cat utility')
parser.add_argument('filename', nargs='+', help="input file")

args = parser.parse_args()

with open('output', 'w') as outfile:
	for file in args.filename:
		with open(file) as infile:
			for line in infile:
				outfile.write(line)


with open('outfile', 'r') as f2:
    data = f2.read()
    sys.stdout.write(data) # Using print gives a newline at the end
