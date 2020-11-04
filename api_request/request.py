import tweepy

with open("api_key", "r") as f:
    api_key = f.read()

with open("api_key_secret", "r") as f:
    api_key_secret = f.read()

auth = tweepy.OAuthHandler(api_key, api_key_secret)

# token = session.get('request_token')
# session.delete('request_token')
# auth.request_token = { 'oauth_token' : token,
#                          'oauth_token_secret' : verifier }

# try:
#     auth.get_access_token(verifier)
# except tweepy.TweepError:
#     print('Error! Failed to get access token.')

api = tweepy.API(auth)





print("Test request")
for tweet in tweepy.Cursor(api.search, q='trump').items(10):
    print(tweet.text)
print("-----------")

# Stream Listener

class MyStreamListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        print(str(raw_data))

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:

            return False


class MyStream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, track):
        self.stream.filter(track=track, is_async=True)


listener = MyStreamListener()
stream = MyStream(api.auth, listener)
stream.start(['python'])
