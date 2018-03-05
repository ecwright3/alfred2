from controller import DbHandler
import importlib
import settings
import os
import glob
import collections
from modules import DigitalOcean as service
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
        KeyStatus = DbHandler.listKeys(self.database)
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
    def buildServer(self):
        InfKey = DbHandler.getKey(
            database=self.database,
            keyName=self.InfrastructureService
            )
        
        token = InfKey[0][1]
        result =  service.InfrastructureService().create_server(token=token)
        
        #Send details to Resources Table


        #Send Action to log Table

        return result   



