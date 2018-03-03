import sqlite3
import os




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

#Check for existing databases.  This is a  job of the controller. The controller is respnsible for telling teh DBHandler which Database to work with. 
#The DbHandler is responsible for performing CRUD operations for any database passed to it.  

#DbHandler Functions

##Database Functions
#   Create Database
#   Drop Database
#   Rename Database


##Table Functions
#   Create Table
#   Update Table
#   Rename Table
#   Drop Table(s)
#   Insert Row(s)
#   Update Row(s)
#   Select Row(s)
#   Delete Row(s)    
#   


##View Functions
#   Create View 
#   Rename View
#   Drop View(s)
#   Select Row(s)