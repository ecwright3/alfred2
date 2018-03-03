from controller import DbHandler
import settings
import modules
#import settings


class mySettings():
    
    def __init__(self):
        self.database = DbHandler.initialize()
        self.InfrastructureService = settings.InfrastructureService
        self.MailService = settings.MailService
        self.StorageService = settings.StorageService
        self.Twitter = settings.Twitter
        self.GooglePlus = settings.GooglePlus
        self.Facebook = settings.Facebook
        self.Instagram = settings.Instagram
        self.Slack = settings.Slack 




