import tweepy

bearer_token = ""

#search four cities

class TweetListener(tweepy.StreamingClient):

    def on_tweet(self, tweet: tweepy.Tweet):
        tweet = dict(tweet)

        tweet['city'] = 'Brisbane'
        tweet['created_at'] = str(tweet['created_at'])
        #tweet['emotion'] = te.get_emotion(tweet['text'])

        print(tweet)


    def on_request_error(self, status_code):
        print(status_code)
    
    def on_connection_error(self):
        self.disconnect()

if __name__ == "__main__":
    client = TweetListener(bearer_token)

    rules = [tweepy.StreamRule(value='(brisbane OR Kangaroo Point OR New Farm OR Fortitude Valley OR Highgate Hill OR West End OR Spring Hill OR Auchenflower OR Taringa OR Annerley) -is:retweet -is:reply lang:en')]

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
    try:
        client.filter(tweet_fields=['created_at'])
    except KeyboardInterrupt:
        client.disconnect()
