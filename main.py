from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime
import os
import flask
import random

#################################
#                               #
# Set up the teitter API        #
#                               #
#################################
consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET_KEY"]
#access_token=""
#access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

#################################
#                               #
# (temp) Hardcode list of food  #
#                               #
#################################
recipes = ['Cake', 'Cookie', 'Pie', 'Jumbolaya', 'Burrito', 'Quesadilla', 'Sandwich', 'Omlette', 'Pancakes', 'Waffles']


#################################
#                               #
# Dynamically create the page   #
#                               #
#################################
app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():
    # Initialize the variables being passed to the html with flask to default values
    keyword = recipes[random.randint(0,len(recipes)-1)]
    tweet_content = "Hello world"
    tweet_sender = "AI"
    tweet_date = "the future"
    image_url = "/static/origami_dragon.jpg"
    recipe_url = "https://www.google.com/"
    name_recipe = "Search Google for more " + keyword + " ideas"
    
    # TODO get a tweet relevant to the keyword and overwrite the default values of the flask variables
    max_tweets = 1
    for relevant_tweet in Cursor(auth_api.search, q=keyword, count=1).items(max_tweets):
        tweet_content = relevant_tweet.text
        tweet_sender = relevant_tweet.user.name + " (@" + relevant_tweet.user.screen_name + ")"
        tweet_date = relevant_tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
    
    # TODO get a corresponding recipe and image from Spoontacular and overwrite the default values of the flask variables
    
    # Plug the flask variables into the render template and return the page
    return flask.render_template(
        "index.html",
        recipe_seed = keyword,
        tweet = [tweet_content, tweet_sender, tweet_date],
        recipe_image = image_url,
        recipe_link = recipe_url,
        recipe_name = name_recipe
        )

#################################
#                               #
# Open and Display the Page     #
#                               #
#################################
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True # TODO: turn off debug before submitting to Hiroku
    )
