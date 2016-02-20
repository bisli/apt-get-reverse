#!/usr/bin/env python

import argparse
import logging
import subprocess
from sys import argv
from collections import namedtuple
import fileinput
import re
import datetime
import pdb


LOG_FILE_PATH = '/var/log/apt/history.log'

def comStructToCommand(com_struct):
    if com_struct.Type == "Install":
        return "sudo apt-get purge " + ' '.join(com_struct.Packages)
    elif com_struct.Type == "Remove" or com_struct.Type == "Purge":
        return "sudo apt-get install " + ' '.join(com_struct.Packages)
    else:
        return ""

def logParser(command):

    ComStruct = namedtuple("ComStruct", "StartDate Type Packages")

    if ("Upgrade: " in command):
        return None

    fields = command.split("\n")

    if len(fields) < 3:
        return None

    time = datetime.datetime.strptime(fields[0].split(": ")[1], "%Y-%m-%d %H:%M:%S")
    commandType = fields[2].split(": ")[0]
    packages = filter(lambda x: ", automatic" not in x, fields[2].split(": ")[1].split("), "))
    packages = map(lambda x: re.sub(r'\(.*', '', x), packages)

    return ComStruct(StartDate = time, Type = commandType, Packages = packages)



def main(timeInHours):

    lower_bound_time = datetime.datetime.now() - datetime.timedelta(hours = int(timeInHours))
    logfile = open(LOG_FILE_PATH, 'r')  #accepts the 2nd parameter as the input for parsing.
    commands = logfile.read()[1:].split("\n\n")
    command_structs = filter(lambda x: x != None, map(logParser, commands))
    command_structs = filter(lambda x: x.StartDate > lower_bound_time, command_structs)
    commands = map(comStructToCommand, command_structs)

    if dryrun_toggle:
        print "Commands to run:"
        for command in commands:
            print "  " + command.strip()
    else:
        for command in commands:
            subprocess.call(command.strip().split(' '))


# Create a parser to take in STDIN arguments
parser = argparse.ArgumentParser()

# Add the time argument
parser.add_argument("timeInHours")
parser.add_argument("-d", action="store_true") # dry run toggle 

# Put the arguments of the parser into the var args
args = parser.parse_args()

if __name__ == "__main__":
    main(args.timeInHours, args.d)