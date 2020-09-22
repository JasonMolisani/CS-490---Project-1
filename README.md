# Find a Recipe
Jason Molisani's (jm979) project 1

## How to get the code running
1. Open a terminal, command window, or some other form of bash shell and navigate to the main folder of the repository.
2. Load a valid twitter api key and corresponding sercret key into the TWITTER_API_KEY and TWITTER_API_SECRET_KEY environmental variables.
   - I have been doing this manually by copying and pasting from a local file since it feels more secure to not save the keys in some cloud that I don't have control over.
3. Run the code from the terminal by entering 'python main.py'

## Technical Problems encountered
1. So far I have yet to run into any real problems. The biggest issue was my unfamiliarity with tweepy, but a couple internet searches allowed my to find the syntax needed. My code ran on the first try.
2. The closest I have come to a problem occured during homework 4, where flask kept going out of its way to find the stylesheet used in the example from class instead of the stylesheet I had made for the homework. Both stylesheets had exactly the same name and containing folder name, but the containing folders themselves were in different folders. I still don't know why flask wanted to move up three levels and then down three levels from the index.html file instead of just up and down one level (or just down 1 level from the terminal's current directory with the executing main.py). I "solved" this by using unique names for all my css files. Technically I first encountered this problem in the homework, but I would have eventually run into it in the project if I wasn't already using unique filenames.

## Known Issues and Possible improvements
- The search of tweets can sometimes return tweets that are not in english. This happens most often when the tweet tags another user and their username/handle contains part of the keyword.
  - Currently unresolved
- The web page looks very ugly. The css file has been linked, but the file itself remains empty
  - Currently unresolved
- Spoontacular not implemented
  - Currently unresolved - part of Milestone two
