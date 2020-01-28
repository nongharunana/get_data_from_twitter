from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from pythainlp import word_tokenize

name = '@BTS_SkyTrain'
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def crawler():
    count = 0
    for status in tweepy.Cursor(api.user_timeline, screen_name=name, tweet_mode="extended").items():
        if count > 4:
            break
        messages = status.full_text.splitlines()
        proc = ''
        matching = []
        noti = ''
        time = ''
        for i in messages:
            proc = word_tokenize(i, engine='newmm')
            matching = [s for s in proc if ('ขัดข้อง' in s) or (
                'ขออภัย' in s) or ('ขณะนี้' in s) or ('ความไม่สะดวก' in s) or ('ตามปกติ' in s)]
                
            print(matching)
            if len(matching) != 0:
                noti = status.full_text
                time = status.created_at
                # break
        if noti != '':
            break

        # f.write(f'index:{count} message:{status.full_text}')
        count += 1
    print(noti)
    print(time)
    return noti, time

crawler()