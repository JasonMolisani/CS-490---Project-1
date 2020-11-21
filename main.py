import os
import flask
import random
from tweepyHandler import TweepyHandler
from spoonHandler import SpoonHandeler

app = flask.Flask(__name__)

@app.route('/')
def index():
    # Select a keyword to use for the seed of twitter and spoonacular search
    recipes = ['Cake', 'Cookie', 'Pie', 'Jumbolaya', 'Burrito', 'Quesadilla', 'Sandwich', 'Omlette', 'Pancakes', 'Waffles']
    keyword = recipes[random.randint(0,len(recipes)-1)]
    
    # Get values for the flask variables
    spoon_handler = SpoonHandeler()
    recipe = spoon_handler.getRecipeAbout(keyword, fake_error=False)
    tweepy_handler = TweepyHandler()
    tweet = tweepy_handler.getTweetAbout(keyword, fake_error=recipe['error'])
    
    # Bundle the variables into a dictionary to pass info Flask
    flask_vars = {
        'recipe_seed': keyword,
        'tweet': [tweet['content'], tweet['sender'], tweet['date']],
        'recipe_image': recipe['imageUrl'],
        'recipe_link': recipe['recipeUrl'],
        'recipe_name': recipe['name'],
        'ingredients': recipe['ingredients'],
        'num_ingredients': len(recipe['ingredients']),
        'prep': recipe['prepTime']
    }
    
    # Plug the flask variables into the render template and return the page
    return flask.render_template(
        "index.html",
        **flask_vars
        )

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = False
    )
