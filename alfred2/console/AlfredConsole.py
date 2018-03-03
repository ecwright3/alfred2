from cmd import Cmd
from resources import art 
import os


class AlfredConsole(Cmd, object):
    intro = art.main()

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit

    def do_show(self, args):
        """
        Displays information about the Alfred console
        
        Avalible Show Options:
        ==============================================
        banner
        resources

        """
        options = ['banner', 'resources']

        if len(args) == 0:
            print("You need to tell me what to show.")
        if args.lower() not in options:
            print("%s is not a valid command" %args)
        
        if args.lower() == "banner":
            art.main()            
                