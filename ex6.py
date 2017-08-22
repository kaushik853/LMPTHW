import argparse
import os
import glob
from stat import S_ISREG
import subprocess
import shlex

parser = argparse.ArgumentParser(description='Copy the find utility')
parser.add_argument('directory', help="directory to search")
parser.add_argument('--name', help="regex for names to search")
parser.add_argument('--type', help="type of file to search. d = directory, f = regular file, l = symbolic link")
parser.add_argument('--print', action="store_true", dest="printfiles", help="print names of found files")
parser.add_argument('--exec', action="store", dest="exec_command", help="execute command on found files")
args = parser.parse_args()

#1. The directory to start searching in: . or /usr/local/
directory = os.path.abspath(os.path.realpath(os.path.expanduser(args.directory)))

if not os.path.isdir(directory):
    print(directory, "is not a directory")
    os._exit(1)
else:
    print("Searching", directory)

os.chdir(directory)
#2. A filter argument like -name or -type d (files of type directory).
namefiles = []
if args.name:
    #print("Looking for pattern", args.name, "in", os.getcwd())
    #print("Found",glob.glob(args.name))
    for file in glob.glob(args.name):
        namefiles.append(file)

typefiles = []
if args.type:
    if args.type == "d":
        for file in os.listdir():
            if os.path.isdir(file):
                typefiles.append(file)
    elif args.type == "f":
        for file in os.listdir():
            if os.path.isfile(file):
                st = os.lstat(file)
                if S_ISREG(st.st_mode):
                    typefiles.append(file)
    elif args.type == "l":
        for file in os.listdir():
            if os.path.isfile(file):
                st = os.lstat(file)
                if not S_ISREG(st.st_mode):
                    typefiles.append(file)
    #print("Files of type",args.type,"are",typefiles)

files = []
if args.name and args.type:
    files = list(set(namefiles) & set(typefiles))

if args.name and not args.type:
    files = namefiles

if args.type and not args.name:
    files = typefiles

#3. An action to do with each found file: -print.
if args.printfiles:
    for file in files:
        print(file)

if args.exec_command:
    for file in files:
        #split the command to be executed into a list
        command = shlex.split(args.exec_command)
        #find and replace {} with the found filename
        command = [w.replace('{}', file) for w in command]
        #print("Trying to run", command)
        completed = subprocess.run(command)
        #print('returncode:', completed.returncode)

#TODO: The exec command won't expand relative pathnames so will fail with "cp {} ~/Desktop"
#Don't know how to make it smart enough to recognize paths in an arbitrary command