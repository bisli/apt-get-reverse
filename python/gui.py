#! /usr/bin/env python3

import locale
import pdb
import main
from dialog import Dialog
import datetime as dt
import os



def choiceVec(timeInHours):
    comms = []
    (commands, packages, times) = main.logParser()
    datetimeToGoBackTo = dt.datetime.now() - dt.timedelta(hours = timeInHours)
    for x in range(0, len(commands)):
        if (times[x] > datetimeToGoBackTo):
            comms.append((packages[x] + "- " +commands[x], '',True))
    return comms

def convertCommand(command):
    if command == 'Install':
        return 'purge'
    elif command == 'Purge':
        return 'install'
    elif command == 'Remove':
        return 'install'
    return ''


# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog")
# Dialog.set_background_title() requires pythondialog 2.13 or later
d.set_background_title("teg-tpa")


# In pythondialog 3.x, you can compare the return code to d.OK, Dialog.OK or
# "ok" (same object). In pythondialog 2.x, you have to use d.DIALOG_OK, which
# is deprecated since version 3.0.0.
if d.yesno("Are you REALLY sure you want to use this?") == d.DIALOG_OK:

    time = d.inputbox("Enter how much time you want to go back? (hours)")
    time = float(time[1])

    comms = choiceVec(time)

    if len(comms) <= 0:
        d.msgbox("No Packages Modified")
    else:
        # We could put non-empty items here (not only the tag for each entry)
        code, tags = d.checklist("What changes do you want to remove?",
                                 width=65,
                                 choices=comms,
                                 title="press SPACE to toggle selection?",
                                 backtitle="teg-tpa")
        if code == d.DIALOG_OK:
            final_apt_commands = []
            for tag in tags:
                (package, command) = tag.split(" - ")
                os.system("sudo apt-get " + convertCommand(command) + " " + package)
            # 'tags' now contains a list of the toppings chosen by the user
            #pdb.set_trace()
            pass
        tarball = d.yesno("Do you want to back up the /etc/ path?")
        if tarball == d.DIALOG_OK:
            print "compressing"
