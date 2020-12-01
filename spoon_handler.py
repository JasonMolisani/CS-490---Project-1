'''
Class to house and wrap the spoonacular API and the specific searches I wish to execute
'''
import os
from os.path import join, dirname
from dotenv import load_dotenv
import spoonacular as sp


class SpoonHandler:
    '''
    custom wrapper for spoonacular API
    '''
    def __init__(self):
        dotenv_path = join(dirname(__file__), "tweepy.env")
        load_dotenv(dotenv_path)
        spoon_key = os.environ["SPOONACULAR_API_KEY"]
        self.sp_api = sp.API(spoon_key)

    def get_recipe_about(self, keyword, fake_error=False):
        '''
        Get a recipe related to keyword and return a dictionary with that a link to that
        recipe, a link to the image of what the recipe makes, the recipe's name, the time
        needed to make the recipe, number of ingredients, and a list of those ingredients.
        There is also an error field that indicates whether the API request completed
        smoothly. If there is an error, default values will be returned.

        The optional fake_error parameter can be used to bypass the API call and return the
        default values.
        '''
        try:
            if fake_error:
                raise Exception()
            sp_response = self.sp_api.search_recipes_complex(keyword, number=1)
            sp_response = sp_response.json()["results"][0]
            sp_data = self.sp_api.get_recipe_information(sp_response["id"])
            sp_data = sp_data.json()
            image_url = sp_data["image"]
            recipe_url = sp_data["sourceUrl"]
            name_recipe = sp_data["title"]
            prep_time = sp_data["readyInMinutes"]
            ingredient_list = []
            for ingrd in sp_data["extendedIngredients"]:
                ingredient_list.append(ingrd["original"])
            spoon_error = False
        except:
            image_url = "/static/origami_dragon.jpg"
            recipe_url = "https://www.instructables.com/id/How-To-Make-a-Perfect-Peanut-Butter-and-Jelly-Sand/"
            name_recipe = (
                "Sorry we couldn't find an interesting recipe. Here's how to make PB&J"
            )
            prep_time = "1"
            ingredient_list = ["2 Slices of Bread", "Peanut Butter", "Jelly (or Jam)"]
            spoon_error = True
        return {
            "imageUrl": image_url,
            "recipeUrl": recipe_url,
            "name": name_recipe,
            "prepTime": prep_time,
            "ingredients": ingredient_list,
            "numIngredients": len(ingredient_list),
            "error": spoon_error,
        }
