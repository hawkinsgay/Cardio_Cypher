import tweepy
from time import sleep
from API.credentials import *
from API.config import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

# Step_up Number of Queries to check:
tweets_per_query = 50

# Set_up Retweet Settings:
for tweet in tweepy.Cursor(api.search, q=Q1 or Q2 or Q3 or Q4 or Q5 or Q6 or Q7
                           or Q8 or Q9 or Q10 or Q11 or Q12 or Q13 or Q14 or Q15).items(tweets_per_query):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        if LIKE:
            tweet.favorite()
            print('Favorited the tweet')

        # Follow the user who tweeted
        # check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')

        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
