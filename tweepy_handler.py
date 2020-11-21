'''
Class to house and wrap the tweepy API and the specific searches I wish to execute
'''
import os
from os.path import join, dirname
from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor


class TweepyHandler:
    '''
    custom wrapper for tweepy API
    '''
    def __init__(self):
        dotenv_path = join(dirname(__file__), "tweepy.env")
        load_dotenv(dotenv_path)
        consumer_key = os.environ["TWITTER_API_KEY"]
        consumer_secret = os.environ["TWITTER_API_SECRET_KEY"]

        auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth_api = API(auth)

    def get_tweet_about(self, keyword, fake_error=False):
        '''
        Get a tweet containing keyword and return a dictionary with that tweet's content
        sender and date. There is also an error field that indicates whether the API
        request completed smoothly. If there is an error, default values will be returned.

        The optional fake_error parameter can be used to bypass the API call and return the
        default values.
        '''
        try:
            if fake_error:
                raise Exception()
            max_tweets = 1
            for relevant_tweet in Cursor(
                self.auth_api.search,
                q=keyword,
                count=1,
                tweet_mode="extended",
                lang="en",
            ).items(max_tweets):
                try:
                    tweet_content = relevant_tweet.retweeted_status.full_text
                except AttributeError:  # Not a Retweet
                    tweet_content = relevant_tweet.full_text
                tweet_sender = (
                    relevant_tweet.user.name
                    + " (@"
                    + relevant_tweet.user.screen_name
                    + ")"
                )
                tweet_date = relevant_tweet.created_at.strftime(
                    "%m/%d/%Y, %H:%M:%S %Z GMT"
                )
            tweet_error = False
        except:
            tweet_content = "Hello world. There's nothing to be worried about. We mean you no harm"
            tweet_sender = "AI"
            tweet_date = (datetime.now() + timedelta(days=1)).strftime(
                "%m/%d/%Y, %H:%M:%S GMT"
            )
            tweet_error = True
        return {
            "content": tweet_content,
            "sender": tweet_sender,
            "date": tweet_date,
            "error": tweet_error,
        }
