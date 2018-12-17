import random

def main():
    secret = random.randint(1, 15)
    while True:
        guess = int(raw_input("Make your Choice between 1 and 15:"))
        if guess == secret:
            print("YEAH you are lucky the number is %s!!!" % secret)

        else:
            print("tut uns leid, das war leider nichts.. bitte versuche es erneut")


if __name__ == "__main__":
    main()




