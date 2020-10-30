#Assignment 10: Part 1
#Jay Anderson
#12/5/2018
#python
#section 002

#Open up the data file and read in the movie review date
file = open("movie_reviews.txt", "r")
data = str.lower( file.read() )
file.close()


# split the reviews into a list of strings
allreviews = data.split("\n")



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
        if c.isalnum() or c == " ":
            clean_review += c


    #isolate each word
    words = clean_review.split(" ")

    #visit every word in this review and update our dictionary to
    #hold info about it
    for w in words:
        if w not in sentiment:
            sentiment[w] = [ rating, 1 ]

        else:
            sentiment[w][0] += rating
            sentiment[w][1] += 1

phrase = input("Enter a word to test: ") #i really hate being hungry
words = phrase.split(" ")

total = 0
num = 0

#visit every  word
for w in words:
    #do we know about this word in our sentiment dict
    if w in sentiment:
        #print(w, sentiment[w], sentiment[w][0]/sentiment[w][1])
        print("'", w, "'", " appears ", sentiment[w][1], " times", sep = "")
        print("The average score for reviews containing the word ", "'", w, "'", " is ", sentiment[w][0]/sentiment[w][1], sep ="")
    

        total += sentiment[w][0]/sentiment[w][1]
        num+=1
    else:
        print("'", w, "'", " appears 0 times", sep = "")
        print("There is no average score for reviews containing the word ", "'", w, "'", sep = "") 

if num > 0:
    
    if total/num > 2:
        print("This is a positive word")
    elif total/num < 2:
        print("This is a negative word")
    elif total/num == 2:
        print("This is a neutral word")

        


else:
    print("Cannot determine if this word is positive or negative")



