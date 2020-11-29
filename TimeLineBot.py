import tweepy
import datetime
import threading

def check_time(curr_hour):
    dt = datetime.datetime.now()

    if curr_hour != dt.hour:
        print(dt)
        curr_hour = dt.hour

        consumer_Key = ""
        consumer_secret = ""

        access_token = ""
        access_toekn_secret = ""

        auth = tweepy.OAuthHandler(consumer_Key,consumer_secret)

        auth.set_access_token(access_token,access_toekn_secret)

        api = tweepy.API(auth)

        hour = 0

        if curr_hour == 0:
            hour = 24
        else:
            hour = curr_hour

        tweet = "Now : "
        tweet += str(hour)
        tweet += "시 "
        tweet += str(dt.minute)
        tweet += "분 "
        tweet += str(dt.second)
        tweet += "초."

        api.update_status(status=tweet)
        print("Successfully Posted")

    threading.Timer(1, check_time, args=[curr_hour]).start()

if __name__ == '__main__':
    check_time(-1)
