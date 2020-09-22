# project1-jm979
Jason Molisani's project 1

# How to get the code running
1. Open a terminal, command window, or some other form of bash shell and navigate to the main folder of the repository.
2. Load a valid twitter api key and corresponding sercret key into the TWITTER_API_KEY and TWITTER_API_SECRET_KEY environmental variables.
 - I have been doing this manually by copying and pasting from a local file since it feels more secure to not save the keys in some cloud that I don't have control over.
3. Run the code from the terminal by entering 'python main.py'

# Technical Problems encountered
So far I have yet to run into any real problems. The biggest issue was my unfamiliarity with tweepy, but a couple internet searches allowed my to find the syntax needed. My code ran on the first try.

# Known Issues and Possible improvements
- The search of tweets can sometimes return tweets that are not in english. This happens most often when the tweet tags another user and their username/handle contains part of the keyword.
-- Currently unresolved
- The web page looks very ugly. The css file has been linked, but the file itself remains empty
-- Currently unresolved
- Spoontacular not implemented
-- Currently unresolved - part of Milestone two
