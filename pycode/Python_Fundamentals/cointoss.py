import random
def cointoss():
    print "Starting the program..."
    count_heads = 0
    count_tails = 0
    for count in range (1, 5001):
        prob = round(random.random())
        result = ""
        if prob == 0:
            result += "head"
            count_heads += 1
        elif prob == 1:
            result += "tails"
            count_tails += 1
        print "Attempt #" + str(count) + ": Throwing a coin... It's a " + result + "! ... Got " + str(count_heads) + " head(s) so far and " + str(count_tails) + " tail(s) so far"
    print "Ending the program, thank you!"
    return cointoss

print cointoss()
