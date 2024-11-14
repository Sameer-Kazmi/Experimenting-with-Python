'''
Question for if, elif and else:
Ques) Write a program to check whether an year is a leap year or not.
'''
Year=int(input("Enter the Year: "))  #Taking year as input from the user.
if Year%100==0:  #Checking the divisibility by 400 condition.
    if Year%400==0:
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
elif Year%4==0:  #Checking the divisibility by 4 condition.
    print("Leap Year.")
else:
    print("Not a Leap Year.")
