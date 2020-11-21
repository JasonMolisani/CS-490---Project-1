'''
This hosts a webpage that, on refresh, dynamically chooses a keyword from a hard-coded list and
displays a tweet and spoonacular recipe related to that keyword
'''

import os
import random
import flask
from tweepy_handler import TweepyHandler
from spoon_handler import SpoonHandeler

APP = flask.Flask(__name__)


@APP.route("/")
def index():
    '''
    Generate the html to host at the '/' address
    '''
    # Select a keyword to use for the seed of twitter and spoonacular search
    recipes = [
        "Cake",
        "Cookie",
        "Pie",
        "Jumbolaya",
        "Burrito",
        "Quesadilla",
        "Sandwich",
        "Omlette",
        "Pancakes",
        "Waffles",
    ]
    keyword = recipes[random.randint(0, len(recipes) - 1)]

    # Get values for the flask variables
    spoon_handler = SpoonHandeler()
    recipe = spoon_handler.get_recipe_about(keyword, fake_error=True)
    tweepy_handler = TweepyHandler()
    tweet = tweepy_handler.get_tweet_about(keyword, fake_error=recipe["error"])

    # Bundle the variables into a dictionary to pass info Flask
    flask_vars = {
        "recipe_seed": keyword,
        "tweet": [tweet["content"], tweet["sender"], tweet["date"]],
        "recipe_image": recipe["imageUrl"],
        "recipe_link": recipe["recipeUrl"],
        "recipe_name": recipe["name"],
        "ingredients": recipe["ingredients"],
        "num_ingredients": recipe["numIngredients"],
        "prep": recipe["prepTime"],
    }

    # Plug the flask variables into the render template and return the page
    return flask.render_template("index.html", **flask_vars)


APP.run(port=int(os.getenv("PORT", "8080")), host=os.getenv("IP", "0.0.0.0"), debug=False)
