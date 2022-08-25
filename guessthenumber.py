def main():
    import time
    nolist=["no", "n"]
    yeslist=["yes", "y"]
    print(" ")
    print("$$$$$$$$$WELCOME TO MY NUMBER GUESSING GAME$$$$$$$$$")
    time.sleep(3)
    print(" ")
    print("...............................................")
    print("..................CONTROLES....................")
    print("...............................................")
    print("...............yes, y / no, n .................")
    print("...............................................")
    print(" ")
    time.sleep(3)
    print("...............................................")
    print("................Instructions...................")
    print("...............................................")
    print("..........Write Down A 3Digit Number...........")
    print("...............................................")
    print("................!!!WARNING!!!..................")
    print("..............always answer yes................")
    print("...............................................")
    time.sleep(9)
    print(" ")
    print("Ready To Become My Bishh")
    time.sleep(6)
    print(" ")
    first_question = input("Did You Write Your Numbers Down?")
    if first_question in yeslist:
        time.sleep(1)
        print(" ")
        print("Then Turn The Numbers The Other Way Around And Put The First 3Digit Number Above The Second One")
    else:
        print(" ")
        print("START WRITING BISHH!!!")
        time.sleep(1)
        main()
    print(" ")
    second_question = input("Done?")
    if second_question in yeslist:
        time.sleep(1)
        print(" ")
        print("After You Did That Subtract The First 3Digits By The Second 3Digits And Then You Have Your Final Number")
        time.sleep(4)
    else:
        print(" ")
        print("Haha You Tryna Fuck With Me?")
        print(" ")
        time.sleep(4)
        print("I'll Keep Throwing You Into Loops So Think Twice Next Time")
        print(" ")
        time.sleep(5)
        main()
    print(" ")
    print("So Now That You yHave Your Final 3Digit Number I'll Guess It Simply By Asking For Just One Of The 3Digits")
    print("If Your Left With Only 2 Digits Type 0 When Asked For First Digit")
    print(" ")
    time.sleep(9)
main()
                        #GAME LOGIC
import time
first_inp = input("Enter Your First Digit And Let The Magic Start(000): ")
three_digit_answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if input not in three_digit_answer:
    first_number = int(first_inp) * 100
    definitive_number = int(90)
    third_number = int(9) - int(first_inp)
    answer = int(first_number) + int(definitive_number) + int(third_number)
    print("YOUR DIGITS ARE:")
    time.sleep(3)
    print(" ")
    print("*******")
    print("*", answer, "*")
    print("*******")
else:
    print("YOUR DIGITS ARE:")
    time.sleep(3)
    print(" ")
    print("***")
    print("*99*")
    print("***")


nolist=["no", "n"]
yeslist=["yes", "y"]

last_question = input("Do You Want To Play Again?")
if last_question in yeslist:
    main()
else:
    exit()