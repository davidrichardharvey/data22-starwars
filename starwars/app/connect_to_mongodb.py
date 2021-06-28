from pymongo.errors import ConnectionFailure
import pymongo


#  Using the pymongo module to connect to MongoDB and select the starwars database.
client = pymongo.MongoClient()
db = client["starwars"]


#  Originally written as a test, I instead put the client connection in a try-except clause.
#  This can inform the user that they must run the daemon in order to connect.
def connect_to_db():
    #  Using the global variable for client as it can be defined outside of the function.
    global client
    try:
        #  A low-impact command is run to test the connection went through, as there is no longer a ConnectionFailure
        #  from running the MongoClient() constructor.
        client.admin.command('ismaster')
        print("Successfully connected to the starwars database.")
        pass
    except ConnectionFailure:
        print("Failed to connect to the database.\n"
              "Please connect to the MongoDB daemon by using mongod in your bash terminal.")
