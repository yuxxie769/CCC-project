#导入tweepy
from itertools import count
import tweepy
import json
import text2emotion as te
 
#填写twitter提供的开发Key和secret
consumer_key = 'aCEEadkvw7NVPl09Nnvtfd62C'
consumer_secret = 'ehgIHf9rKiN01eP9Qg87ecKfWXIY3TauY4omTeJdpXA4fc3ikt'
access_token = '1516335562843586562-EMM6i877VEWr4mFjYntolWVp0mJGcv'
access_token_secret = '2DZJNN8GdpD77l1oqFujagDLqhxlGFot5lyRLnmokeW8X'
 
#提交你的Key和secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
#获取类似于内容句柄的东西
api = tweepy.API(auth)
results     = []
key_words = '(crime OR criminal OR robbery OR theft OR murder OR illegal OR stab OR drug OR victims OR victim OR injured OR shooting OR police OR died OR dead OR casualty OR flames OR fire)'
file_name = 'crime_results_30days.json'
#search four cities
cities = ['Melbourne','Sydney','Brisbane','Adelaide']
start_time = "202203280000"
end_time = "202204270000"
maxResults = 100
num_page = 30
count_request = 0
#public_tweets = api.search_30_day('dev','(crime OR criminal OR robbery OR theft OR murder OR illegal) place:Melbourne',fromDate="202204010000", toDate="202204200000",maxResults=10)
#for i in range(len(key_words)):
for j in range(len(cities)):
    for page in tweepy.Cursor(api.search_30_day,'dev', key_words +' place:' + cities[j]+' lang:en', fromDate=start_time, toDate=end_time, maxResults=maxResults).pages(num_page):
        count_request += 1
        print('request '+str(count_request))
        for tweet in page:
            #print (tweet.created_at)
            #check the tweet is retweet or not
            if tweet.text.startswith("RT") and tweet.retweeted_status != None:
                isRT = True
            else:
                isRT = False
            #get full text
            if(hasattr(tweet,'extended_tweet')):                                        
                #print (tweet.extended_tweet['full_text'])
                text = tweet.extended_tweet['full_text']
            else:
                #print(tweet.text)
                text = tweet.text
            
            #rearrange the tweet data
            obj = {
                '_id' : tweet.id,
                'user_id' : tweet.author.id,
                'text' : text,
                'created_at' : str(tweet.created_at),
                'city' : cities[j],
                'is_retweet' : isRT,
                'emotion' : te.get_emotion(text)
            }
            results.append(obj)
        print ("----------")
print(len(results))
#write json file
with open(file_name,'w',encoding='utf-8') as f:
    f.write(json.dumps({'docs':results}))
#print(len(public_tweets))


