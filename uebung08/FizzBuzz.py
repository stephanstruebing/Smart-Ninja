print "FizzBuzz, lass uns loslegen"

zahl = raw_input("Bitte gib eine Zahl zwischen 1 und 100 ein: ")



zahl = int(zahl)

for i in range(1, zahl+1):
        if i % 3 == 0 and i % 5 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i
