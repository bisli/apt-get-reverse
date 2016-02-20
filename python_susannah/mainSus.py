#!/usr/bin/env python

import argparse
import subprocess
import datetime as dt
import pdb


# LOG_FILE_PATH = '/var/log/apt/history.log'
LOG_FILE_PATH = 'susLog.log'



def logParser():

    commands = []
    programs = []
    startDatetimes = []

    f=open(LOG_FILE_PATH,'r')
    lines = f.readlines()
    
    for i in range(0, len(lines)):
        
        line = lines[i]
        if line[0] == '\n':
            continue
        elif line.split(':')[0] == 'Start-Date':
            startLineNumber = i
            continue
        elif line.split(':')[0] == 'End-Date':
            endLineNumber = i

            if startLineNumber and endLineNumber:
                if (startLineNumber + 1) < endLineNumber:

                    for i in range(startLineNumber+1, endLineNumber):
                        command = lines[i].split(':')[0]
                        if command in ('Install','Purge','Remove'):
                            startDatetime_str = lines[startLineNumber].split(' ')[1] + ' ' + lines[startLineNumber].split(' ')[3][:-1]
                            startDatetime = dt.datetime.strptime(startDatetime_str, '%Y-%m-%d %H:%M:%S')
                            program = lines[i].split(' ')[1]

                            print command, program, startDatetime
                            commands.append(command)
                            programs.append(program)
                            startDatetimes.append(startDatetime)

                else:
                    # No data in this set, so try the next.
                    continue

    return (commands,programs,startDatetimes)


def convertCommands(commands):

    for i in range(0, len(commands)):

        command = commands[i]

        if command == 'Install':
            command = 'purge'
        elif command == 'Purge':
            command = 'install'
        elif command == 'Remove':
            command = 'install'

        commands[i] = command

    return (commands)


def main(timeInHours):

    (commands,programs,startDatetimes) = logParser()
    # Convert commands to their negatives to be executed
    (commands) = convertCommands(commands)

    datetimeToGoBackTo = dt.datetime.now() - dt.timedelta(hours = float(timeInHours))

    diffs = []
    for i in range(0, len(startDatetimes)):
        diffs.append(abs(datetimeToGoBackTo - startDatetimes[i]))

    index_closestDate = diffs.index(min(diffs))

    commands_inDateRange = commands[index_closestDate:]
    programs_inDateRange = programs[index_closestDate:]

    for i in range(0, len(commands_inDateRange)):
        print("%sing %s" % (commands_inDateRange[i], programs_inDateRange[i]))
        subprocess.call(["sudo", "apt-get", "%s" % commands[i], "%s" % programs[i]])

    subprocess.call(["sudo", "apt-get", "autoclean"])
    subprocess.call(["sudo", "apt-get", "clean"])
    

# Create a parser to take in STDIN arguments
parser = argparse.ArgumentParser()

# Add the time argument
parser.add_argument("timeInHours")

# Put the arguments of the parser into the var args
args = parser.parse_args()

if __name__ == "__main__":
    main(args.timeInHours)