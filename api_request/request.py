import tweepy

with open("api_key.txt", "r") as f:
    api_key = f.read()

with open("api_key_secret.txt", "r") as f:
    api_key_secret = f.read()

with open("access_token.txt", "r") as f:
    access_token = f.read()

with open("access_token_secret.txt", "r") as f:
    access_token_secret = f.read()

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)



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
