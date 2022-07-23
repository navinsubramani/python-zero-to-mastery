import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
bearer_token = ''
user_id = 123

client = tweepy.Client(bearer_token, consumer_key,
                       consumer_secret, access_token, access_token_secret)


followers = client.get_users_followers(user_id)
print(len(followers.data))
for user in followers.data:
    pass
    # print(user)


tweets = client.get_users_mentions(user_id)
for tweet in tweets:
    print(tweet)
