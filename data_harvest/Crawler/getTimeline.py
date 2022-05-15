import json
import tweepy

# This program is for gathering 7news and 9news twitter account timeline tweets.
# login
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAANIabgEAAAAAi0itUDUbKqDZywnxqEUO8wqGBXI%3Dd7Mc2YYOAC6jeG5Zo7QCJYUuDtUPZ5QsnEJq7LlNxvVB0GwAiM')

maxResults = 100
num_page = 32
# Prepair user list
accountNameList = ['7newsmelbourne','7newssydney','7newsbrisbane','7newsadelaide','9newsmelb','9newssyd','9newsadel','9newsqueensland']
accountIdList = ['121639467','156464691','74382140','269581619','183036128','171802941','259506084','36255721']
key_words = ['crime','criminal','robbery','theft','murder','illegal','stab','drug','victims','victim','injured','shooting','shootings','police','died','dead','casualty','flames','fire']
results     = []
# search all users' timeline
for index,accountId in enumerate(accountIdList):
    next_token = None
    #The Maximum return tweews of one request is 100, therefore we need get next 100 tweews by adding next_token in request.
    #Repeat 32 times to get up to 3200 tweews per user because the uppper limit of API is 3200 per user.
    for page in range(num_page):
        tweets = client.get_users_tweets(id=accountId,tweet_fields=['created_at'],pagination_token=next_token, exclude='retweets',max_results = maxResults)
        next_token = tweets.meta.get("next_token")        
        #print(next_token)
        for tweet in tweets.data:
            tweet = dict(tweet)
            for keyword in key_words:
                if (tweet['text'].lower().find(keyword) != -1):
                        tweet['_id'] = str(tweet['id'])
                        tweet.pop('id')
                        tweet['created_at'] = str(tweet['created_at'])
                        if (index < 4):
                            tweet['media'] = '7news'
                        else:
                            tweet['media'] = '9news'
                        if (index == 0 or index == 4):
                            tweet['city'] = 'Melbourne'
                        elif (index == 1 or index == 5):
                            tweet['city'] = 'Sydney'
                        elif (index == 2 or index == 6):
                            tweet['city'] = 'Brisbane'
                        else:
                            tweet['city'] = 'Adelaide'
                        results.append(tweet)
                        break
        if (next_token == None):
            break
print('total qualified tweets '+str(len(results)))

#push files to couchdb
with open('NewsTimeLine.json','w',encoding='utf-8') as f:
            f.write(json.dumps({'docs':results}))
            print('NewsTimeLine.json is finished')
