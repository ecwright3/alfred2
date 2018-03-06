from controller import DbHandler
import importlib
import settings
import os
import glob
import collections
import uuid
from modules import DigitalOcean as service


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

    def listResources(self):
          resourceList = DbHandler.listResources(self.database)
          resourceTable = """
-----------------------------------------------------------------------------------------------------------------
ResourceName       |      Date Created       | Time | Resource Type |     IP Address    |  Configuration Type   |
----------------------------------------------------------------------------------------------------------------- 
 """
          for r in resourceList:
              
              resourceTable += """
%s |    %s |    %s  |    %s     |    %s |                       |
-----------------------------------------------------------------------------------------------------------------               
              """ % (r[0], r[1], r[2], r[3], r[4])

          return resourceTable       
    
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
        DbHandler.addResource(
            database=self.database,
            resource=result
        )
        #Send Action to log Table

        #eventUid,eventDate,eventTitle,severity,eventName,user,message, eventSource
        message = "%s - instance id: %s, Ip address(%s), was created" %(result['name'], result['id'], result['ip_address'])
        serverName = result['name']
        eventId = str(uuid.uuid4())
        entry = (eventId, result['created_at'],'New Server Created','INFO',result['name'],'', message,'alfCore.buildServer',)
        
        DbHandler.addLogEntry(
            database=self.database,
            entry=entry
        )

        return result   



