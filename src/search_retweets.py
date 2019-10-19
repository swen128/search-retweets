import pickle
from os import environ

import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
id = 1165959742784540673
author = '@__P_N_D__'
original_tweet = """にじさんじの配信で「えらい」とコメントされた回数を集計して動画で表現しました

アイコンがでかい程えらい

#しいなーと"""

query = f'{original_tweet} filter:retweets {author}'
cursor = tweepy.Cursor(api.search, q=query, since_id=id, count=100)
retweets = list(cursor.items())

out_path = 'resources/retweets.pickle'

with open(out_path, mode='wb') as f:
    pickle.dump(retweets, f)
