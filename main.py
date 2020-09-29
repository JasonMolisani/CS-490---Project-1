from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv
from os.path import join, dirname
import os
import flask
import random
import spoonacular as sp

#################################
#                               #
# Set up the twitter API        #
# Set up the spoonacular API    #
#                               #
#################################
dotenv_path = join(dirname(__file__), 'tweepy.env')
load_dotenv(dotenv_path)
consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET_KEY"]
spoon_key = os.environ["SPOONACULAR_API_KEY"]
#access_token=""
#access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

sp_api = sp.API(spoon_key)


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
    tweet_content = "Hello world. There is nothing to be worried about. We mean you no harm :)"
    tweet_sender = "AI"
    tweet_date = (datetime.now() + timedelta(days=1)).strftime("%m/%d/%Y, %H:%M:%S GMT")
    image_url = "/static/origami_dragon.jpg"
    recipe_url = "https://www.instructables.com/id/How-To-Make-a-Perfect-Peanut-Butter-and-Jelly-Sand/"
    name_recipe = "Sorry we couldn't find an interesting recipe. Here's how to make PB&J"
    ingredient_list = ["2 Slices of Bread", "Peanut Butter", "Jelly (or Jam)"]
    prep_time = "1"
    
    # # get a tweet relevant to the keyword and overwrite the default values of the flask variables
    # max_tweets = 1
    # for relevant_tweet in Cursor(auth_api.search, q=keyword, count=1).items(max_tweets):
    #     try:
    #         tweet_content = relevant_tweet.retweeted_status.full_text
    #     except AttributeError:  # Not a Retweet
    #         tweet_content = relevant_tweet.text
    #     tweet_sender = relevant_tweet.user.name + " (@" + relevant_tweet.user.screen_name + ")"
    #     tweet_date = relevant_tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S %Z")
    
    # # get a corresponding recipe and image from Spoontacular and overwrite the default values of the flask variables
    # sp_response = sp_api.search_recipes_complex(keyword, number=1)
    # sp_response = sp_response.json()["results"][0]
    # sp_data = sp_api.get_recipe_information(sp_response["id"])
    # sp_data = sp_data.json()
    # image_url = sp_data["image"]
    # recipe_url = sp_data["sourceUrl"]
    # name_recipe = sp_data["title"]
    
    # Bundle the variables into a dictionary to pass info Flask
    flask_vars = {
        'recipe_seed': keyword,
        'tweet': [tweet_content, tweet_sender, tweet_date],
        'recipe_image': image_url,
        'recipe_link': recipe_url,
        'recipe_name': name_recipe,
        'ingredients': ingredient_list,
        'num_ingredients': len(ingredient_list),
        'prep': prep_time
    }
    
    # Plug the flask variables into the render template and return the page
    return flask.render_template(
        "index.html",
        **flask_vars
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
