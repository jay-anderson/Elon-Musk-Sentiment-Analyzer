#Assignment 10: Part 4
#Jay Anderson
#12/7/2018
#section 002
#python


import time
starttime = time.time()

#Open up the data file and read in the movie review date
file = open("movie_reviews.txt", "r")
data = str.lower( file.read() )
file.close()


# split the reviews into a list of strings
allreviews = data.split("\n")



#set up a dictionary to hold all our words
sentiment_dict = {}


print("Initializing sentiment database")
number_w = 0

for review in allreviews:
    #extract the rating for this review
    rating = int(review[0])
    
    #extract the rest of the review
    rest = review[2:].lower()

    #clean up the review

    clean_review = ""
    for c in rest:
        if c.isalpha() or c == " ":
            clean_review += c


    #isolate each word
    words = clean_review.split(" ")

    #visit every word in this review and update our dictionary to
    #hold info about it
    for w in words:
        if w not in sentiment_dict:
            sentiment_dict[w] = [ rating, 1 ]
            number_w += 1
        else:
            sentiment_dict[w][0] += rating
            sentiment_dict[w][1] += 1

if "" in sentiment_dict:
	del sentiment_dict[""]

def sentiment(phrase):
    phrase = phrase.lower()
    clean_phrase = ""

#i think the issue with it not reutrning thanks as 3.0
#is here but if i change it it doesn't do the 2nd
#example right
    for c in phrase:
        if c.isalnum() or c == " ":
            clean_phrase += c


    words = clean_phrase.split(" ")
#    words = phrase.split(" ")
############################
    total = 0
    num = 0

    #visit every  word
    for w in words:
        #do we know about this word in our sentiment dict
        if w in sentiment_dict:
            total += sentiment_dict[w][0]/sentiment_dict[w][1]

            num+=1

    if num > 0:
        
        return total/num
    if num == 0:
        return 0 

print("Sentiment database initialization complete")
print("Total unique words analyzed:", number_w)
endtime = time.time()
print("Analysis took", endtime - starttime, "seconds to complete")
print()

 
print()
user_year = input("Enter a year in YY format: ")

user_month = input("Enter a month (1-2 digits): ")
print()
#get data to analyze aka elon's tweets
file = open("elonmusk_tweets_class.txt", "r")
elon_data = ( file.read() )
file.close()
#might need to import regex
import re


#Open up the Elon Musk tweets and iterate through each one, one line at a time

alltweets = elon_data.split("\n")

elon_tweets = []
number = 0
# ATTENTION: iterate through alltweets
for tweet in alltweets:
    # use if and in statements to find user input in
    # tweets
    if user_month in tweet[0:2] and user_year in tweet[4:8]:
    # add 'successful' tweets to lists
        clean_tweet = ""
        for c in tweet:
            clean_tweet += c
        tweets = clean_tweet.split("\n")
        elon_tweets += tweets
        number += 1


#if they are the same, send the tweet portion to your function and compute the sentiment score
avg_sentiments = []
elon_rest = []


for tweets in elon_tweets:
    
    rest = (tweets.split("|||")[1])

    clean_rest = ""
    for c in rest:
        clean_rest += c
    new_rest = clean_rest.split(" ")
    elon_rest += new_rest

    first_avglist = ""
    first_avglist += str(sentiment(rest))

    
    sec_avglist = ""
    for c in first_avglist:
        sec_avglist += c
    third_avg = sec_avglist.split(" ")
    avg_sentiments += third_avg

return_elon = []
for tweets in elon_tweets:
    rest = (tweets.split("|||")[1])
    final_rest = ""
    for c in rest:
        final_rest += c
    comp_rest = final_rest.split("\n")
    return_elon += comp_rest

float_sentiments = list(map(float, avg_sentiments))

if float_sentiments:
    most_pos = (max(float_sentiments))
    max_index = float_sentiments.index(most_pos)


    print("During this period there were", number, "tweets")
    print("Most positive tweet rated at", most_pos)
    print(return_elon[max_index])
elif not float_sentiments:
    print("During this period there were 0 tweets")

