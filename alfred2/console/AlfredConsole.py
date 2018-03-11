from cmd import Cmd
from resources import resources
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

        if args.lower() == "resources":
            resourcesList = Control.listResources()
            print(resourcesList)    


    def do_build(self, args):
        """ Create infrastructure """

        options = ['server']

        if len(args) == 0:
            print("You have to tell me what we are building. Please Try again.")
        if args.lower().strip() not in options:
            print("%s, is not a valid command" %args)
        
        if args.lower().strip() == "server":
            server = Control.buildServer()
            print(server)


    def do_import(self, args):
        """ 
Import resources and keys 

Avalible Import Options
==================================
server\t key\t resource
        """
        options = ['server','key','resource']
        #request = list(filter(lambda x: str(x).lower().strip() in options, args)) 
        if len(args) == 0:
            print("You have to tell me what you want to import. Please try again.")     
        
        elif args == "server":
            a =  input("Would you like to add a server from %s?(y/n)" %Control.InfrastructureService)
            if a.lower().strip()[0] == 'y':
                print("collecting details....\n")
                cloudServers = Control.listCspServers()
                print(cloudServers)


    
                