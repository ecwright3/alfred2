import sqlite3
import os
import uuid
import glob


#+++++++++++++++++++++++++++++++++++++++++  Standard Alfred Database Objects  ++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------------------------------------------------#
#                                                      TABLES                                                           #
#=======================================================================================================================#
#   resource  - resourceUid, instanceName, instanceId, resourceType, dateCreated, ipAddress, configurationType          #
#   keys      - keyUid, name, user, key, keyType(API/PGP/SSHPriv/SSHPub/password), dateStored, baseDestinationUrl       #
#   logs      - eventUid, severity(debug/info/warn/error), eventName message, eventDate, user, componentSource          #
#-----------------------------------------------------------------------------------------------------------------------#
#                                                                                                                       #
#                                                      VIEWS                                                            #
#=======================================================================================================================#
#   v_resoures - instanceName,dateCreated,resourceType,ipaddress,configurationType                                      #
#   v_keys     - name, dateStored, keyType, user, baseDestinationUrl                                                    #
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



def create(name='alf'):
    """
    Creates a new Sqlite3 database.
    """
    #Check If a database already exists
    dbDirPath = os.path.join(os.path.dirname(__file__), '..\storage')
    dbList = glob.glob("%s\*.db" %dbDirPath)
    if len(dbList) > 0 :
        dbPath = dbList[0]
    else:
        dbName ="%s_%s.db"%(str(name).lower().strip(),str(uuid.uuid4()))
        dbPath = os.path.join(os.path.dirname(__file__), '..\storage\%s' %dbName)
        conn = sqlite3.connect(dbPath)
    return dbPath    

test = create("test")
print(test)
