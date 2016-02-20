#!/usr/bin/env python
# encoding: utf-8

(RECENTLY_INTALLED, RECENTLY_REMOVED) = getVals()

RECENTLY_INSTALLED = ['Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3','Choice 1', 'Choice 2', 'Choice 3']
RECENTLY_REMOVED = ['Choice 1', 'Choice 2', 'Choice 3']

import npyscreen
import pdb
class TestApp(npyscreen.NPSApp):
    def main(self):
        Options = npyscreen.OptionList()

        # just for convenience so we don't have to keep writing Options.options
        options = Options.options

        options.append(npyscreen.OptionMultiChoice('Recently Installed Files to Remove', choices=RECENTLY_INSTALLED))
        options.append(npyscreen.OptionMultiChoice('Recently Removed Files to Install', choices=RECENTLY_REMOVED))

        try:
            Options.reload_from_file('/tmp/test')
    	except:
        	pass

        F  = npyscreen.Form(name = "Welcome to Npyscreen",)

        ms = F.add(npyscreen.OptionListDisplay, name="Option List",
                values = options,
                scroll_exit=True,
                max_height=None)

        F.edit()

        Options.write_to_file('/tmp/test')

if __name__ == "__main__":
    App = TestApp()
    App.run()