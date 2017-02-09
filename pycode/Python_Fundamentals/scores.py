import random

def score():
    for count in range (0,10):
        randomnum = random.randint(60,101)
        if randomnum <= 69:
            print "Score: " + str(randomnum) + "; Your grade is D"
        elif (randomnum >=70 and randomnum <=79):
            print "Score: " + str(randomnum) + "; Your grade is C"
        elif (randomnum >=80 and randomnum <=89):
            print "Score: " + str(randomnum) + "; Your grade is B"
        elif (randomnum >=90 and randomnum <=100):
            print "Score: " + str(randomnum) + "; Your grade is A"
    print "End of the program, bye!"
    return score

print score()
