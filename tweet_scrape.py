# import relevant python packages
import tweepy
import csv

import html
# define consumer keys and API keys by assigning them to a variable
consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

# authenticate twitter handle for verifying identity using tweepy functions
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# create variable for inputing search term
sw = input('Enter Search Term:',)

# assign search word inputed by user to search_words tweepy function
search_words = sw + "-filter:retweets"
# define time frame for data collected (within 14 days)
date_since = ""
date_until = ""

# create variable for user to input how many tweets they want
tweetno = input('How many tweets do you want?',)
# convert user input to integer
tweetno = int(tweetno)

# define tweets variable based on Twitter request for API search
# Include and define all relevant variables
tweets = tweepy.Cursor(api.search, truncated = False, q=search_words, lang="en", wait_on_rate_limit = True, tweet_mode = "extended").items(tweetno)

# open and create a file to append the data to
csvFile = open('.csv', 'a')
csvWriter = csv.writer(csvFile)
    # use the csv file
    # loop through the tweets variable and add contents to the CSV file
for tweet in tweets:
    text = tweet.full_text.strip()
    #convert the text to ascii ignoring all unicode characters, eg. emojis
    text_ascii = text.encode('ascii','ignore').decode()
    #split the text on whitespace and newlines into a list of words
    text_list = text_ascii.split()
    #iterate over the words, removing @ mentions or URLs (word.startswith('@') or
    text_list_filtered = [word for word in text_list if not (word.startswith('@')
    or word.startswith('http'))]
    #join the list back into a string
    text_filtered = ' '.join(text_list_filtered)
    #decoding html escaped characters
    text_filtered = html.unescape(text_filtered)
    #write text to the CVS file
    #  tweet.place
    csvWriter.writerow([tweet.created_at, text_filtered])
    print(tweet.created_at, text_filtered)
csvFile.close()
