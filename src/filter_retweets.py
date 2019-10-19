import tweepy
import pickle

out_path = 'resources/retweets.pickle'

with open(out_path, mode='rb') as f:
    retweets = pickle.load(f)


def is_influential(tweet: tweepy.Status) -> bool:
    return tweet.author.followers_count > 10000


influential_retweets = list(filter(is_influential, retweets))
influential_authors = [rt.author.name for rt in influential_retweets]

original_tweet = '''RT @__P_N_D__: にじさんじの配信で「えらい」とコメントされた回数を集計して動画で表現しました

アイコンがでかい程えらい

#しいなーと https://t.co/adKqI4Vk0C'''

retweets_with_comments = [rt for rt in retweets if rt.text != original_tweet]
