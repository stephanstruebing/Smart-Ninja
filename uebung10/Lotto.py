import random

print ("Welcome to the Lottery generator.")

while True:
    random_numbers_list = []

    number_of_num = int(raw_input("Please enter how many random numbers between 1 and 50 would you like to have: "))

    random_numbers = random.sample(range(1, 51), k=number_of_num)
    random_numbers_list.append(random_numbers)
    print random_numbers

    again = raw_input("Would you like to try again? (yes/no)")

    if again == "yes":
        continue
    elif again == "y":
        continue
    else:
        break

print ("Here are your generated numbers: " + str(random_numbers_list))
print ("END")
