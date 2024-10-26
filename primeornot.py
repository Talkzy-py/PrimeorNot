yournumber = int(input("What is your number? "))
howmanydivisors = yournumber
howmanydivisors = howmanydivisors + 1
alldivisors = []
divisors = []
for i in range(howmanydivisors):
    if i != 0:
        alldivisors.append(i)
for i in alldivisors:
    if i == 0:
        alldivisors.remove
for i in alldivisors:
    oddoreven = yournumber % i
    if oddoreven == 0:
        divisors.append(i)
        if len(divisors) > 2:
            break
if len(divisors) <= 2:
    print("Your number is prime, it can only be divided by:", divisors)
if len(divisors) > 2:
    print("Your number is not prime, it can be divided by:", divisors)