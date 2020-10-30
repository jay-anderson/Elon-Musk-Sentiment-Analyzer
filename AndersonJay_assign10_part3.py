#Assignment 10: Part 3
#Jay Anderson
#section 002
#12/5/2018
#python

#create a function called 'sentiment' that takes one
#argument - a string of data.

#Open up the data file and read in the movie review date
file = open("movie_reviews.txt", "r")
data = str.lower( file.read() )
file.close()


# split the reviews into a list of strings
allreviews = data.split("\n")



#set up a dictionary to hold all our words
sentiment_dict = {}



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

        else:
            sentiment_dict[w][0] += rating
            sentiment_dict[w][1] += 1


if "" in sentiment_dict:
    del sentiment_dict[""]

def sentiment(phrase):
    phrase = phrase.lower()
    clean_phrase = ""
    for c in phrase:
        if c.isalpha() or c == " ":
            clean_phrase += c


    words = clean_phrase.split(" ")
    total = 0
    num = 0

    #visit every  word
    for w in words:
        #do we know about this word in our sentiment dict
        if w in sentiment_dict:
            total += sentiment_dict[w][0]/sentiment_dict[w][1]
            num+=1

    return total/num            
 



###########
#test
a1 = sentiment("The happy dog and the sad cat")
a2 = sentiment("It made me want to poke out my eyeballs")
a3 = sentiment("I loved this movie!")

print (a1, a2, a3) # 2.280133625200816 1.768915591909414 2.07085642181999


