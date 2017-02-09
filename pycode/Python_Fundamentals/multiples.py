for number in range (1, 1001):
    if number % 2 != 0:
        print number

for number in range (5, 1000001):
    if number % 5 == 0:
        print number


xyz = [1,6,7,19,30,2,1]
print sum(xyz)

def mean(numbers):
    return float(sum(numbers)) / len(numbers)

print mean(xyz)
