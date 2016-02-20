from sys import argv
from collections import namedtuple
import fileinput
import re
import datetime

ComStruct = namedtuple("ComStruct", "StartDate Type Packages")

def command_handle(command):
    if ("Upgrade: " in command):
        return None

    fields = command.split("\n")
    
    time = datetime.datetime.strptime(fields[0].split(": ")[1], "%Y-%m-%d %H:%M:%S")
    commandType = fields[2].split(": ")[0]
    packages = re.sub(r'\([^)]*\)', '', fields[2].split(": ")[1]).split(", ")

    return ComStruct(StartDate = time, Type = commandType, Packages = packages)



logfile = open(argv[1], 'r')  #accepts the 2nd parameter as the input for parsing.
commands = logfile.read()[1:].split("\n\n")
command_structs = map(command_handle, commands)