print ("Hello User, please wait the for the Converter to Start")
#print ("Please input the Kilometer value:")
user_input = True

while user_input:
    kilometer = int(raw_input("Please input the kilometer value:"))

    miles = kilometer * 0.621371

    print (miles)

    while True:

        dummy = raw_input("Another input, Sir/Lady? (y/n)? :")

        if dummy == 'y':
            break
        elif dummy == 'n':
            user_input = False
            break
