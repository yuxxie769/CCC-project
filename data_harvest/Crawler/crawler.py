import tweepy
import text2emotion as te
import couchdb
import time
import json
#This program is for 7 days topic-relate twitter harvest.
#login
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAANIabgEAAAAAi0itUDUbKqDZywnxqEUO8wqGBXI%3Dd7Mc2YYOAC6jeG5Zo7QCJYUuDtUPZ5QsnEJq7LlNxvVB0GwAiM')

#Search queries for 1.Crime 2.Income 3.Disabled.
key_words = ['(crime OR criminal OR robbery OR theft OR murder OR illegal OR stab OR drug OR victims OR victim OR injured OR shooting OR police OR died OR dead OR casualty OR flames OR fire)',
             '(rent OR price OR cost OR payment) (house OR housing OR apartment OR residence OR mansion OR residence)',
             '(buy OR pay OR purchase OR afford OR affordable) (can OR able OR capable)',
             '(buy OR pay OR purchase OR afford OR affordable) (can\'t OR cannot OR unable OR incapable)',
             '(buy OR pay OR purchase OR afford OR affordable) (want OR wanted OR wish OR like)',
             '(Disability OR DSP OR disabled)']
#output file name
file_name = ['crime_results', 'rant_results', '','','income_results', 'disabled_results']
#search four cities
citykey = ['(Melbourne OR #Melbourne)','(Sydney OR #Sydney)','(Brisbane OR #Brisbane)','(Adelaide OR #Adelaide)']
cities = ['Melbourne','Sydney','Brisbane','Adelaide']

maxResults = 100
num_page = 20
#login couchdb
masternode='172.26.130.224'
user='Yingpei'
passeord='030988'
url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'
couch = couchdb.Server(url)

#Search 7 days topic-related tweets
#Search all queries
for i in range(len(key_words)):
    if i != 3 and i != 4:
        results = []
    #Search 4 cites
    for j in range(len(citykey)):
        search_turn = 0
        next_token = None
        query = key_words[i] + ' ' + citykey[j] + ' -is:retweet lang:en'
        #The Maximum return tweews of one request is 100, therefore we need get next 100 tweews by adding next_token in request.
        #Repeat 20 times to get up to 2000 tweews per city per query
        for page in range(num_page):
            tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], next_token=next_token,
                                                 max_results=maxResults)
            next_token = tweets.meta.get("next_token")
            print(next_token)
            search_turn += 1
            if tweets.data != None:
                # Reconstruct data sturcture for later output JSON file
                for tweet in tweets.data:
                    tweet = dict(tweet)
                    if i == 2:
                        tweet['income'] = 'can'
                    elif i == 3:
                        tweet['income'] = 'cannot'
                    elif i == 4:
                        tweet['income'] = 'want'
                    tweet['_id'] = str(tweet['id'])
                    tweet.pop('id')
                    tweet['city'] = cities[j]
                    tweet['created_at'] = str(tweet['created_at'])
                    # Emotion analysis on tweet text
                    tweet['emotion'] = te.get_emotion(tweet['text'])
                    results.append(tweet)
            if (next_token == None):
                break
        print('number of turn for each city in every topic: ' + str(search_turn))

    print(len(results))
    # write json files
    if i != 3 and i != 2:
        print(i)
        with open(file_name[i]+'.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps({'new_edits': False, 'docs': results}))

dblist=['rant','crime','disabled','income']
#push files to couchdb
for i in dblist:
    try:
        db = couch[i]
    except:
        couch.create(i)
        db = couch[i]
        print('no such db, created one')
    finally:
        with open(i+'_results.json','r',encoding='utf-8') as f:
            dic = json.load(f)
        documents = db.update(dic['docs'])



