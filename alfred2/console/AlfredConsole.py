from cmd import Cmd
from resources import resources
from controller import controller 
import os
import pprint
pp = pprint.PrettyPrinter(indent=5)

Control = controller.alfCore()

class AlfredConsole(Cmd, object):
    intro = resources.art.main() 
    #controller.alfCore()

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit

    def do_show(self, args):
        """         
Displays information about the Alfred console\n
Avalible Show Options:
==============================================
banner\t resources
         """
        options = ['banner', 'resources', 'settings']

        if len(args) == 0:
            print("You need to tell me what to show.")
        if args.lower() not in options:
            print("%s is not a valid command" %args)
        
        if args.lower() == "banner":
            resources.art.main()  

        if args.lower() == "settings":
            curSetting = Control.showSettings()
            pp.pprint(curSetting)

  
                          
    
                