# Find a Recipe
Jason Molisani's (jm979) project 1

## How to get the code running
<sub><sup>Instructions borrowed and adapted from https://github.com/Sresht/lect6-heroku/blob/master/README</sub></sup>  
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
7. Install python-dotenv using the same commands used in step four, replacing "tweepy" with "python-dotenv"
8. Add your secret keys (from step 2) by making a new file called tweepy.env in the main folder of the repository and populating it as follows. ** MAKE SURE THE FILE AND VARIABLES ARE NAMED THE EXACT SAME WAY AS DESCRIBED!!!**
   - TWITTER_API_KEY='insert_key_here'
   - TWITTER_API_SECRET_KEY='insert_secret_key_here'
8. Run `python main.py`
10. If on Cloud9, preview templates/index.html. This should successfully render the HTML!

## Technical Problems encountered
1. So far I have yet to run into any real problems. The biggest issue was my unfamiliarity with tweepy, but a couple internet searches allowed my to find the syntax needed. My code ran on the first try.
2. The closest I have come to a problem occured during homework 4, where flask kept going out of its way to find the stylesheet used in the example from class instead of the stylesheet I had made for the homework. Both stylesheets had exactly the same name and containing folder name, but the containing folders themselves were in different folders. I still don't know why flask wanted to move up three levels and then down three levels from the index.html file instead of just up and down one level (or just down 1 level from the terminal's current directory with the executing main.py). I "solved" this by using unique names for all my css files. Technically I first encountered this problem in the homework, but I would have eventually run into it in the project if I wasn't already using unique filenames.

## Known Issues and Possible improvements
- The search of tweets can sometimes return tweets that are not in english. This happens most often when the tweet tags another user and their username/handle contains part of the keyword.
  - **Currently unresolved**
- The web page looks very ugly. The css file has been linked, but the file itself remains empty
  - **Partially resolved** - Some css has been entered, but there is still room for improvement
- Spoontacular not implemented
  - **Currently unresolved** - part of Milestone two
