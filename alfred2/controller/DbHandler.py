import sqlite3
import os
import uuid
import glob


#+++++++++++++++++++++++++++++++++++++++++  Standard Alfred Database Objects  ++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------------------------------------------------#
#                                                      TABLES                                                           #
#=======================================================================================================================#
# resources - resourceUid,instanceName,instanceId,resourceType,dateCreated,timeCreated,ipAddress,configurationType      #
# keys      - keyUid, keyName, keyUser, keyText, keyType(API/PGP/SSHPriv/SSHPub/password), dateStored, baseUrl          #
# logs      - eventUid, severity(debug/info/warn/error), eventName message, eventDate, user, eventSource                #
#-----------------------------------------------------------------------------------------------------------------------#
#                                                                                                                       #
#                                                      VIEWS                                                            #
#=======================================================================================================================#
#   v_resoures - instanceName,dateCreated,resourceType,ipaddress,configurationType                                      #
#   v_keys     - keyName, keyUser, dateStored, keyType, baseUrl                                                               #
#   v_logs     - eventDate, severity, eventName, user, message, componentSource                                         #
##---------------------------------------------------------------------------------------------------------------------##

#Check for existing databases. This is a  job of the controller.
#The controller is respnsible for telling teh DBHandler which Database to work with.
#The DbHandler is responsible for performing CRUD operations for any database passed to it.

#DbHandler Functions



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
        (keyUid text, keyName text, keyUser text keyText text, keyType text, dateStored text, timeStored text, baseUrl text)
        '''
        )

        #create v_keys view
        c.execute(''' CREATE VIEW v_keys AS SELECT keyName, dateStored, timeStored, keyType, keyUser, baseUrl FROM keys ''')
        # 
        # 
        #   
        #create logs table
        c.execute(''' CREATE TABLE logs
        (eventUid text, eventDate text, eventTime text, severity text, eventName text, user text, message text, eventSource text)
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

def listKeys(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute( 'SELECT * FROM v_keys')
    keyView = c.fetchall()
    conn.close()

    return keyView

def getKey(database,keyName):
    kn = (keyName,)
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT keyUser, keyText FROM keys WHERE keyName=?', kn)
    myKey = c.fetchall()
    conn.close()
    return myKey

def addResource(database,resource):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    newRuid = str(uuid.uuid4())
            #resourceUid, instanceName, instanceId, resourceType, dateCreated, timeCreated,ipAddress, configurationType
    rDetails = (newRuid,resource['name'],resource['id'],resource['type'],resource['created_at'],'',resource['ip_address'],'',)
    c.execute('INSERT INTO resources VALUES (?,?,?,?,?,?,?,?)', rDetails)
    conn.commit()
    conn.close()

def listResources(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute( 'SELECT * FROM v_resources')
    resourceView = c.fetchall()
    conn.close()

    return resourceView    

#eventUid,eventDate,eventTitle,severity,eventName,user,message, eventSource
def addLogEntry(database,entry):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    #eventUid = str(uuid.uuid4())
    c.execute('INSERT INTO logs VALUES (?,?,?,?,?,?,?,?)',entry)
    conn.commit()
    conn.close()

