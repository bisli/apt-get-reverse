#! /usr/bin/env python3

import locale
import pdb
from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog")
# Dialog.set_background_title() requires pythondialog 2.13 or later
d.set_background_title("teg-tpa")
#commands = ??? (set equal to tuples of every choice)[for checklist]


# In pythondialog 3.x, you can compare the return code to d.OK, Dialog.OK or
# "ok" (same object). In pythondialog 2.x, you have to use d.DIALOG_OK, which
# is deprecated since version 3.0.0.
if d.yesno("Are you REALLY sure you want to use this?") == d.DIALOG_OK:

    time = d.inputbox("Enter how much time you want to go back? (hours)")
    time = int(time[1])



    # We could put non-empty items here (not only the tag for each entry)
    code, tags = d.checklist("What changes do you want to revert?",
                             choices=[("Catsup", "Removal",  False),
                                      ("Mustard", "Removal",  False),
                                      ("Pesto", "Addition",   False),
                                      ("Mayonnaise", "",  True),
                                      ("Horse radish","",  True),
                                      ("Sun-dried tomatoes", "", True)],
                             title="press SPACE to toggle selection?",
                             backtitle="teg-tpa")
    if code == d.DIALOG_OK:
        # 'tags' now contains a list of the toppings chosen by the user
        pass
    tarball = d.yesno("Do you want to back up the /etc/ path?")
    if tarball == d.DIALOG_OK:
        print "compressing"
