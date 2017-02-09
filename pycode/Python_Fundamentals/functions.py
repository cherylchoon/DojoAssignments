def odd_even(a,b):
    for number in range (a, b):
        if number % 2 != 0:
            print "Number is " + str(number) + ". This is an odd number."
        elif number % 2 == 0:
            print "Number is " + str(number) + ". This is an even number."

print odd_even(1,2001)

def multiply(list, a):
    list = [number * a for number in list]
    return list

x = [2,4,5,6]
y = multiply(x,5)
print y

def layered_multiples(func):
    totalArray = []
    for val in func:
        count = 0
        newArray = []
        totalArray.append(newArray)
        while count < val:
            newArray += [1]
            count += 1
    return totalArray

new = layered_multiples(multiply(x, 3))
print new
