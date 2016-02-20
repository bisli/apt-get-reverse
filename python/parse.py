from sys import argv
from collections import namedtuple
import fileinput

ComStruct = namedtuple("StartDate", "Type", "Package", "Dependencies")



logfile = open(argv[1], 'r')  #accepts the 2nd parameter as the input for parsing. 
commands = logfile.read()[1:].split("\n\n")
command_structs = map(command_handle, commands)

    

'''
for line in logfile:
    parts = line.split(':',1)
'''
    
def command_handle(command):
    
    
    


