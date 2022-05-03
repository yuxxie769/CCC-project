import json
import tweepy
import text2emotion as te
import nltk
nltk.download()
 
client = tweepy.Client(bearer_token='')

# Replace with your own search query


key_words = ['(crime OR criminal OR robbery OR theft OR murder OR illegal OR stab OR drug)', '(rent OR price OR cost OR  payment) (house OR housing OR apartment OR residence OR mansion OR residence)', '(buy OR pay OR purchase OR afford OR affordable) (can OR able OR capable)', '(buy OR pay OR purchase OR afford OR affordable) (can\'t OR cannot OR unable OR incapable)', '(buy OR pay OR purchase OR afford OR affordable) (want OR wanted OR wish OR like)', '(Disability OR DSP OR disabled)']
file_name = ['crime_results.json', 'rant_results.json', 'income_can_results.json', 'income_cannot_results.json','income_want_results.json', 'disabled_results.json']
#search four cities
cities = ['Melbourne','Sydney','Brisbane','Adelaide']

maxResults = 100
num_page = 5

#public_tweets = api.search_30_day('30daysEnv','(crime OR criminal OR robbery OR theft OR murder OR illegal) place:Melbourne',fromDate="202204010000", toDate="202204200000",maxResults=10)
for i in range(len(key_words)):
    results     = []
    for j in range(len(cities)):
        search_turn = 0
        next_token = None
        query = key_words[i] +' '+ cities[j] + ' -is:retweet lang:en'
        for page in range(num_page):
            tweets = client.search_recent_tweets(query=query,tweet_fields=['created_at'],next_token=next_token, max_results = maxResults)
            next_token = tweets.meta.get("next_token")        
            print(next_token)
        # Get list of places from includes object
        #places = {p["id"]: p for p in tweets.includes['places']}
            search_turn += 1
    
            for tweet in tweets.data:
                tweet = dict(tweet)
                tweet['city'] = cities[j]
                tweet['created_at'] = str(tweet['created_at'])
                tweet['emotion'] = te.get_emotion(tweet['text'])
                results.append(tweet)
            if (next_token == None):
                break
        print('number of turn: '+str(search_turn))

    print(len(results))
    #write json file
    with open(file_name[i],'w',encoding='utf-8') as f:
        f.write(json.dumps({'new_edits': False,'docs':results}))
    #print(len(public_tweets))


