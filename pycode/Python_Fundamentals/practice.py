str = "If monkeys like bananas, than I must be a monkey!"
print str.find("monkey")
print str.replace("monkey", "alligator")
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[-1]
y = [y[0],y[-1]]
print y
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = []
for number in x:
    if number < 0:
        y.append(number)
print y
x = [i for i in x if i>=0]
print x
x.insert(0,y)
print x
