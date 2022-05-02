# Hanzhen Yang 1070951, 
# Hanzhong Wang, 1029740,
# Quan Zhou 1065302, 
# Yuhang Xie 1089250, 
# Ze Liu 1073628

import tweepy
import json
from tweepy import OAuthHandler
import time
from tweepy.streaming import StreamListener

consumer_key = 'ISXRjwy6li8EGINtzqPjVNFdX'
consumer_secret = '11bWe9Zc4OtfM0A2MX4vIhBRUAKvVgd0cPzF9icjykeYLyIICC'
access_token = '1383630322194026500-myiCV4MnRg4K7bEZNjvLlpfJSBFRf0'
access_secret = 'zIrrjOUxug3eioQ3ZigMlltudA58yuRpXdsd0HdWzshfc'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# search_term = "exercise OR diet OR Yoga OR weightlose OR slim OR gym OR calorie OR muscle OR fatburn"
# search_term = 'bitcoin'
search_term = 'covid OR covid19 OR coronavirus OR covid-19 OR pandemic'
with open("covid_vic.json","w") as f:
    # api.search
    count=0
    # NSW--"-32.238539,147.516999,500km"
    # VIC--"-36.874119,144.634508,500km"
    for tweet in tweepy.Cursor(api.search, q=search_term, geocode = "-36.874119,144.634508,500km", result_type="recent", include_entities=False).items(1000000):
        # print(tweet._json)
        f.write(json.dumps(tweet._json)+"\n")
        count+=1
    f.write("total counts:"+ str(count)+"\n")
