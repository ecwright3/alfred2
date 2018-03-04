from controller import DbHandler
import settings
import modules
import os
import glob
import collections
#import settings


class alfCore():
    
    def __init__(self):
        name = 'alf'
        DbHandler.initialize()
        dbDirPath = os.path.join(os.path.dirname(__file__), '..\storage')
        dbList = glob.glob("%s\%s_*.db" %(dbDirPath, name))
        
        self.database = dbList[0]
        self.InfrastructureService = settings.InfrastructureService
        self.MailService = settings.MailService
        self.StorageService = settings.StorageService        

      
    def showSettings(self):
        KeyStatus = DbHandler.getKeys(self.database)
        keys = {}
        for i in KeyStatus:
            key = {
                "keyName"       : i[0],
                "dateCreated"   : i[1],
                "timeCreated"   : i[2],
                "keyType"       : i[3],
                "userName"      : i[4],
                "urlBase"       : i[5]
            }
            keys[key['keyName']] = key
        return keys
        #return coreSettings
        
    #self.Twitter = settings.Twitter
    #self.GooglePlus = settings.GooglePlus
    #self.Facebook = settings.Facebook
    #self.Instagram = settings.Instagram
    #self.Slack = settings.Slack 




