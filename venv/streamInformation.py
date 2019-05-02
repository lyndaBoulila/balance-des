from tweepy.streaming import StreamListener
from tweepy.streaming import Stream
import time
import auth
import json
from pymongo import MongoClient


#Connexion vers la base de données mongoDB
try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database
db = conn.datbasetestgeo

# Created or Switched to collection names: my_gfg_collection
collection = db.Tweets

#Réccuperer  les tweets

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        id_tweet = all_data["id_str"]
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]

       # print(all_data)  # pour afficher les tweets
        # Insert Data
        print(all_data["user"]["lang"])
        if (all_data["user"]["lang"] == "fr"):
            rec_id = collection.insert_one(all_data)
            print("Data inserted with record ids", rec_id)
            # rec_id2 = collection.insert_one(emp_rec2)



        return True

    def on_error(self, status):
        print(status)


def contains_word(string, word):
    return (' ' + word + ' ') in (' ' + string + ' ')


api, auth = auth.auth()

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#disneyland","#champsElysées","#parcAsterix","#montmartre","#notreDameDeParis","#Dauville","#CoteDAzur","#BassinDArcachan","#MontSaintMichel","#Canne"]) # pour traquer plusieurs mots, faire ["A","B"]
#twitterStream.filter(track=["name"])
#twitterStream.filter(track=["fr"])


# Printing the data inserted
#cursor = collection.find()
#for record in cursor:
#	print(record)
