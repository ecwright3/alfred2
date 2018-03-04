import sqlite3
import os
import uuid
import glob


#+++++++++++++++++++++++++++++++++++++++++  Standard Alfred Database Objects  ++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------------------------------------------------#
#                                                      TABLES                                                           #
#=======================================================================================================================#
#   resources  - resourceUid, instanceName, instanceId, resourceType, dateCreated, ipAddress, configurationType         #
#   keys      - keyUid, keyName, user, keyText, keyType(API/PGP/SSHPriv/SSHPub/password), dateStored, baseUrl           #
#   logs      - eventUid, severity(debug/info/warn/error), eventName message, eventDate, user, eventSource              #
#-----------------------------------------------------------------------------------------------------------------------#
#                                                                                                                       #
#                                                      VIEWS                                                            #
#=======================================================================================================================#
#   v_resoures - instanceName,dateCreated,resourceType,ipaddress,configurationType                                      #
#   v_keys     - keyName, dateStored, keyType, user, baseUrl                                                               #
#   v_logs     - eventDate, severity, eventName, user, message, componentSource                                         #
##---------------------------------------------------------------------------------------------------------------------##

#Check for existing databases. This is a  job of the controller.
#The controller is respnsible for telling teh DBHandler which Database to work with.
#The DbHandler is responsible for performing CRUD operations for any database passed to it.

#DbHandler Functions

##Database Functions
#   Create Database (Done)
#   List Database(s)
#   Drop Database

##Table Functions
#   Create Table
#   Update Table
#   Rename Table
#   Drop Table(s)
#   Insert Row(s)
#   Update Row(s)
#   Select Row(s)
#   Delete Row(s)

##View Functions
#   Create View
#   Rename View
#   Drop View(s)
#   Select Row(s)

##Advanced Function
#   New_AlfredDb


def initialize(database=""):
    if len(database) == 0:
        create()
    
    else:
        conn = sqlite3.connect(database)
        c = conn.cursor()

        #create resources table
        c.execute(''' CREATE TABLE resources
        (resourceUid text, instanceName text, instanceId text, resourceType text, dateCreated text, timeCreated text, ipAddress text, configurationType text)
        '''
        )
        #create v_resource view 
        c.execute(''' CREATE VIEW v_resources AS SELECT instanceName, dateCreated, timeCreated, resourceType, ipAddress, configurationType FROM resources     
        '''
        )

        #create keys table
        c.execute(''' CREATE TABLE keys
        (keyUid text, keyName text, keyText text, keyType text, dateStored text, timeStored text, baseUrl text)
        '''
        )

        #create v_keys view
        c.execute(''' CREATE VIEW v_keys AS SELECT keyName, dateStored, timeStored, keyType, user, baseUrl FROM keys ''')
        # 
        # 
        #   
        #create logs table
        c.execute(''' CREATE TABLE logs
        (eventUid text, eventDate text, eventTime text, severity text, eventName text, user text, meessage text, eventSource text)
        '''
        )
        #create v_logs view
        c.execute( ''' CREATE VIEW v_logs AS SELECT  eventDate, eventTime, severity, eventName, user, message, eventSource FROM logs
        '''

        )



        conn.commit()
        conn.close()
        return database





def create(name='alf'):
    """
    Creates a new Sqlite3 database.
    """
    #Check If a database already exists
    dbDirPath = os.path.join(os.path.dirname(__file__), '..\storage')
    dbList = glob.glob("%s\%s_*.db" %(dbDirPath, name))
    if len(dbList) > 0 :
        dbPath = dbList[0]
    else:
        dbName ="%s_%s.db"%(str(name).lower().strip(),str(uuid.uuid4()))
        dbPath = os.path.join(os.path.dirname(__file__), '..\storage\%s' %dbName)
        #conn = sqlite3.connect(dbPath)
        initialize(dbPath)
    return dbPath    
