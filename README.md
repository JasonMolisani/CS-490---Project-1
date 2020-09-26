# Find a Recipe
Jason Molisani's (jm979) project 1

## How to get the code running on cloud 9
<sup>Instructions borrowed and adapted from https://github.com/Sresht/lect6-heroku/blob/master/README</sup>  
1. Sign up for the twitter developer portal at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
3. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
4. Clone this repository by using git clone http://www.github.com/Sresht/lect6-heroku
5. Install tweepy using one of the following console commands:
   - sudo pip install tweepy
   - sudo pip3 install tweepy
   - pip install tweepy
   - pip3 install tweepy
6. Install flask using the same command used in step four, replacing "tweepy" with "flask"
7. Install spoonacular using the same command used in step four, replacing "spoonacular" with "flask"
8. Install python-dotenv using the same commands used in step four, replacing "tweepy" with "python-dotenv"
9. Add your secret keys (from step 2) by making a new file called tweepy.env in the main folder of the repository and populating it as follows. **MAKE SURE THE FILE AND VARIABLES ARE NAMED THE EXACT SAME WAY AS DESCRIBED!!!**
   - TWITTER_API_KEY='insert_key_here'
   - TWITTER_API_SECRET_KEY='insert_secret_key_here'
10. Run `python main.py`
10. Click the preview button at the top of the screen and select "Preview Running Application" from the drop down

## Technical Problems encountered
1. The first problem actually occured during homework 4, where flask kept going out of its way to find the stylesheet used in the example from class instead of the stylesheet I had made for the homework. Both stylesheets had exactly the same name and containing folder name, but the containing folders themselves were in different folders. I still don't know why flask wanted to move up three levels and then down three levels from the index.html file instead of just up and down one level (or just down 1 level from the terminal's current directory with the executing main.py). I "solved" this by using unique names for all my css files. Even though I encountered this in the homework, I believe I would have eventually run into it in the project if I wasn't already using unique filenames.
2. When getting spoonacular up and runnimg I had issues correctly pulling the dictionary out of the list of results that was encoded in json. It wasn't too difficult to solve with a couple runs, each getting a step further.
3. Accidentally made my background the same color as hyperlinks and spent a minute wondering why the recipe name wasn't appearing. Once identified (using ctrl-a to highlight all and reveal the text), fixing it was a simple css change.

## Known Issues and Possible improvements
- The search of tweets can sometimes return tweets that are not in english. This happens most often when the tweet tags another user and their username/handle contains part of the keyword.
  - **Currently unresolved**
- The web page looks very ugly. The css file has been linked, but the file itself remains empty
  - **Partially resolved** - Some css has been entered, but there is still room for improvement
- Spoontacular not implemented
  - **Resolved** - Basic spoonacular functionality completed
- CSS error, background and the default color of hyperlinks is exactly the same
  - **Currently unresolved** - Finish one thing at a time. Just focus on spoonacular
