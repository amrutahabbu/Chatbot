## ALL THE CONFIGURATIONS GO HERE

import os
import pymongo



def connect_mongoDB():
    # Initialize the client
    try:
        connect_string = "mongodb+srv://dbkhoatrann1998:GHbuiwMymRsTtcPC@dbkhoatrann1998.zbjantr.mongodb.net/?retryWrites=true&w=majority&appName=dbkhoatrann1998"
        mongodb_client = pymongo.MongoClient(connect_string)
    except:
        print('error occured')
    
    # Connect to CIS8045 database 
    db = mongodb_client['CIS8045']
    
    # Connect to collection
    collection = db['data']
    print("Successfully Connected to Mongo DB and use collection data in CIS5045 database")
    
    return collection

def getOpenAIKey():

    api_key = "add_your_key"
    return api_key
