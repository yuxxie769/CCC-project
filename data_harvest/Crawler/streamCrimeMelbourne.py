import tweepy
import couchdb
import time
import sys

masternode='172.26.130.224'
user='Yingpei'
passeord='030988'

url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'


bearer_token = "AAAAAAAAAAAAAAAAAAAAANIabgEAAAAAi0itUDUbKqDZywnxqEUO8wqGBXI%3Dd7Mc2YYOAC6jeG5Zo7QCJYUuDtUPZ5QsnEJq7LlNxvVB0GwAiM"
start_time = time.time()
#search four cities

class TweetListener(tweepy.StreamingClient):

    def on_tweet(self, tweet: tweepy.Tweet):
        tweet = dict(tweet)
        tweet['_id'] = str(tweet['id'])
        tweet.pop('id')
        tweet['city'] = 'Melbourne'
        tweet['created_at'] = str(tweet['created_at'])
        #tweet['emotion'] = te.get_emotion(tweet['text'])
        print(tweet)
        pushData(tweet)
        if (time.time() - start_time) > 43200:
            
            sys.exit()



    def on_request_error(self, status_code):
        print(status_code)
    
    def on_connection_error(self):
        self.disconnect()

def restart():
    try:
        if (time.time() - start_time) > 43200:    
            sys.exit()
        client = TweetListener(bearer_token)
        GetStream(client)
    except KeyboardInterrupt:
        print('keyboard interrupt! exit!')
        client.disconnect()
    except SystemExit:
        print("time up!")
    except:
        restart()

def GetStream(client):

    rules = [tweepy.StreamRule(value='(crime OR criminal OR robbery OR theft OR murder OR illegal OR stab OR drug OR victims OR victim OR injured OR shooting OR police OR died OR dead OR casualty OR flames OR fire) Melbourne -is:retweet -is:reply lang:en')]

    resp = client.get_rules()
    if resp and resp.data:
        rule_ids = []
        for rule in resp.data:
            rule_ids.append(rule.id)
        
        client.delete_rules(rule_ids)

    resp = client.add_rules(rules, dry_run=True)
    if resp.errors:
        raise RuntimeError(resp.errors)
    resp = client.add_rules(rules)
    if resp.errors:
        raise RuntimeError(resp.errors)

  
    print(client.get_rules())
    
    client.filter(tweet_fields=['created_at'])


def pushData(data):
    couch = couchdb.Server(url)
    dbname = 'stream_crime_mel'
    try:
        db = couch[dbname]
    except:
        couch.create(dbname)
        db = couch[dbname]
        print('no such db, created one')
    finally:
        documents = db.update([data])
        print(documents)
        print(dbname +' stream data updated!')

if __name__ == "__main__":
    restart()
