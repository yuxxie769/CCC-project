# Hanzhen Yang 1070951, 
# Hanzhong Wang, 1029740,
# Quan Zhou 1065302, 
# Yuhang Xie 1089250, 
# Ze Liu 1073628

import tweepy

SEP = ';'

csv = open('OutputStreaming.csv','a')
csv.write('Date' + SEP + 'Text' + SEP + 'Location' + SEP + 'Number_Follower' + SEP + 'User_Name' + SEP + 'Friends_count\n')

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        Created = status.created_at.strftime("%Y-%m-%d-%H:%M:%S")
        Text = status.text.replace('\n', ' ').replace('\r', '').replace(SEP, ' ')
        Location = ''
        if status.coordinates is not None:

            lon = status.coordinates['coordinates'][0]
            lat = status.coordinates['coordinates'][1]
            Location = lat + ',' + lon
            Follower = str(status.user.followers_count)
            Name = status.user.screen_name
            Friend = str(status.user.friends_count)

        csv.write(Created + SEP + Text + SEP + Location + SEP + Follower + SEP + Name + SEP + Friend + '\n')

    def on_error(self, status_code):
        print(status_code)

consumer_key = 'ISXRjwy6li8EGINtzqPjVNFdX'
consumer_secret = '11bWe9Zc4OtfM0A2MX4vIhBRUAKvVgd0cPzF9icjykeYLyIICC'
access_token = '1383630322194026500-myiCV4MnRg4K7bEZNjvLlpfJSBFRf0'
access_secret = 'zIrrjOUxug3eioQ3ZigMlltudA58yuRpXdsd0HdWzshfc'

# stream

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

myStream = tweepy.Stream(auth, MyStreamListener())

myStream.filter(track=['good','#Meditation'])
