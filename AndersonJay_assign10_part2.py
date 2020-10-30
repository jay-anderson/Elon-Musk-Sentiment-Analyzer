#Jay Anderson
#Assignment 10: Part 2
#python
#12/4/2018
#section 002

#figure out how to calculate unique words

import time
starttime = time.time()
#Open up the data file and read in the movie review date
file = open("movie_reviews.txt", "r")
data = str.lower( file.read() )
file.close()

print("Initializing sentiment database")


# split the reviews into a list of strings
allreviews = data.split("\n")

number = 0


#set up a dictionary to hold all our words
sentiment = {}

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
        if w not in sentiment:
            sentiment[w] = [ rating, 1 ]
            number += 1

        else:
            sentiment[w][0] += rating
            sentiment[w][1] += 1

if "" in sentiment:
    del sentiment[""]
    
endtime = time.time()
print("Sentiment database initialization complete")
print("Total unique words analyzed:", number)
print("Analysis took", format(endtime - starttime, '.2f') , "seconds to complete")
print()
phrase = input("Enter a phrase to test: ") #i really hate being hungry
words = phrase.split(" ")


total = 0
num = 0

#visit every  word
for w in words:
    #do we know about this word in our sentiment dict
    if w in sentiment:
        #print(w, sentiment[w], sentiment[w][0]/sentiment[w][1])
        print("* ", "'", w, "'", " appears ", sentiment[w][1], " times with an average rating of ", sentiment[w][0]/sentiment[w][1], sep = "")


        total += sentiment[w][0]/sentiment[w][1]
        num+=1
    elif w not in sentiment:
        print("* ", "'", w, "'", " does not have a rating", sep ="")
if num > 0:
    print("Average score for this phrase is:", total/num)
            
    if total/num > 2:
        print("This is a POSITIVE phrase")
    elif total/num < 2:
        print("This is a NEGATIVE phrase")
    elif total/num == 2:
        print("This is a NEUTRAL phrase")
else:
    print("Not enough data to compute sentiment")




