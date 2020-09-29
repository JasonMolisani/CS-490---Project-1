# Find a Recipe
**Jason Molisani's (jm979) CS 490 project 1** - The idea of this project was to make and app that, on page load, will show a random recipe and a related tweet. The app is currently deployed with Heroku here: https://still-taiga-86561.herokuapp.com/

## How to get the code running on cloud 9
<sup>(Instructions borrowed and adapted from https://github.com/Sresht/lect6-heroku/blob/master/README)</sup>
1. Sign up for the twitter developer portal at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
3. Click on the key symbol after creating your project, and it will take you to your keys and tokens (you will need this for step 11).
4. Sign up for a spoonacular account at https://spoonacular.com/food-api
5. Go to My Console and look at your profile. This will let you see your API key (you will need this for step 11).
6. Clone this repository by using the following command in the terminal:
   - git clone http://www.github.com/Sresht/lect6-heroku
7. Install tweepy using one of the following console commands:
   - sudo pip install tweepy
   - sudo pip3 install tweepy
   - pip install tweepy
   - pip3 install tweepy
8. Install flask using the same command used in step 7, replacing "tweepy" with "flask"
9. Install spoonacular using the same command used in step 7, replacing "tweepy" with "spoonacular"
10. Install python-dotenv using the same commands used in step 7, replacing "tweepy" with "python-dotenv"
11. Add your secret keys (from steps 2 and 4) by making a new file called tweepy.env in the main folder of the repository and populating it as follows. **MAKE SURE THE FILE AND VARIABLES ARE NAMED THE EXACT SAME WAY AS DESCRIBED!!!**
    - TWITTER_API_KEY='insert_key_here'
    - TWITTER_API_SECRET_KEY='insert_secret_key_here'
    - SPOONACULAR_API_KEY='insert_spoonacular_api_key_here'
12. Run `python main.py` from the terminal or click the green run button at the top of the cloud 9 IDE
13. Click the preview button at the top of the screen and select "Preview Running Application" from the drop down

## How to deploy this repository to Heroku
<sup>(Instructions borrowed and adapted from https://github.com/Sresht/lect6-heroku/blob/master/README)</sup>
1. Sign up for the twitter developer portal at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
3. Click on the key symbol after creating your project, and it will take you to your keys and tokens (you will need this for step 9).
4. Sign up for a spoonacular account at https://spoonacular.com/food-api
5. Go to My Console and look at your profile. This will let you see your API key (you will need this for step 9).
6. Clone this repository by using the following command in the terminal:
   - git clone http://www.github.com/Sresht/lect6-heroku
7. Sign up for heroku at heroku.com 
8. Run the following commands on the terminal (inputting login information as requred:
   - npm install -g heroku
   - heroku login -i
   - heroku create
   - git push heroku master
9. Add your secret keys (from steps 2 and 4) by going to https://dashboard.heroku.com/apps and clicking into your app. Click on Settings, then scroll to "Config Vars." Click "Reveal Config Vars" and add the key value pairs for each variable in user_tweets.py Your config var key names should be:
   - TWITTER_API_KEY
   - TWITTER_API_SECRET_KEY
   - SPOONACULAR_API_KEY
10. Navigate to your newly-created heroku site by copying and pasting the URL from the end of the "git push heroku master" or clicking the open app button on the Heroku website!


## Technical Problems encountered
1. The first problem actually occured during homework 4, where flask kept going out of its way to find the stylesheet used in the example from class instead of the stylesheet I had made for the homework. Both stylesheets had exactly the same name and containing folder name, but the containing folders themselves were in different folders. I still don't know why flask wanted to move up three levels and then down three levels from the index.html file instead of just up and down one level (or just down 1 level from the terminal's current directory with the executing main.py). I "solved" this by using unique names for all my css files. Even though I encountered this in the homework, I believe I would have eventually run into it in the project if I wasn't already using unique filenames.
2. When getting spoonacular up and runnimg I had issues correctly pulling the dictionary out of the list of results that was encoded in json. It wasn't too difficult to solve with trial and error as I used a combination of print statements and reading the error messages to see what was happening. It turns out that the results were a dictionary mapping "results" to a list of dictionaries, one for each result of the search (all encoded with json). Once I isolated the dictionary of a result, it was relatively easy to pull the desired data looking at the spoonacular documentation (https://spoonacular.com/food-api/docs).
3. Accidentally made my background the same color as hyperlinks and spent a minute wondering why the recipe name wasn't appearing. Once identified (using ctrl-a to highlight all and reveal the text), fixing it was a simple css change.

## Known Issues and Possible improvements
- The search of tweets can sometimes return tweets that are not in english. This happens most often when the tweet tags another user and their username/handle contains part of the keyword.
  - **Currently unresolved**
- The web page looks very ugly. The css file has been linked, but the file itself remains empty
  - **Resolved** - The app now has an accpetable appearance. It could certainly be improved by a more artistic person.
- Spoontacular not implemented
  - **Resolved** - Basic spoonacular functionality completed
- CSS error, background and the default color of hyperlinks is exactly the same
  - **Resolved** - Added a section to the css specifying the color of hyperlinks specifically, since it wasn't inheriting the color from main/body tags.
- Need to adjust web page to include space for recipe prep time and ingredient list
  - **Resolved** - I changed how variables get passed into flask to use a single dictionary of variable_name/value pairs
- Need to pull the ingredient list from spoonacular results to have new values to pass into the spaces created in the updated webpage
  - **Resolved** - This was rather painless after looking at some example responses (https://spoonacular.com/food-api/docs#Get-Recipe-Information). I chose to quote "original" for the list of ingredients since one of the examples tried to link a picture of cheddar cheese for the "grated cheese" ingredient.
- Need to deploy to Heroku
  - **Resolved** - I should point out that the readme instructions don't cover the creation and uses for Procfile and requirements.txt since it assumes the user cloned this repository and therefore has those files already. Procfile exists to tell Heroku what to execute to start the app and requirements.txt tell Heroku what packages it will need to install in order to run the app.
- Need to allow for display of default values if there is an error with the request
  - **Resolved** - (Done as planned) I'll probably use a try/except to do this. First, try to find an appropriate recipe. If that succeeds, look for an appropriate tweet. If spoonacular fails, use all default values. If just twitter fails, use the retrieved spoonacular and the twitter default.
- Need to get full versions of the tweets
  - **Currently Unresolved** - 
- Add time zone to tweet time stamps or convert to local time
  - **Resolved** - Most tweets appear to be stored in GMT by default, so the simple solution is just add " GMT" to the end of the string format
