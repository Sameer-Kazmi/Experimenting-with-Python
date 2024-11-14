'''
For and While loops used with else
Ques) Write a program to check whether a number is prime.
'''
#  Using just For Loop
Num=int(input("Enter a number greater than 1: "))  #Taking an integer from user.
List=[1]  #Using this list and asking the user till the user gives a positive integer.
for i in List:  #Iterating the list.
    if Num<=1:  #Checking whether the number is not greater than 1.
        Num=int(input("Enter a number greater than 1: "))
        List.append(1)  #Adding one element to the list to again execute the for loop.
for i in range(2,int(Num/2)+1):  #Iterating through numbers having a possibility of being a factor.
    if Num%i==0:  #When a factor is encountered, the remainder would become 0.
        print("Not Prime.")
        break  #No need to check the remaining numbers if the number has already been proven not prime.
else:
    print("Prime.")  #This block runs when the whole for loop has been executed showing no possible factors.
#  Using just While Loop
Num=int(input("Enter a number greater than 1: "))  #Taking an integer from the user.
while Num<=1:  #Checking whether the number is not greater than 1.
    Num=int(input("Enter a number greater than 1: "))  #Asking the user repeatedly till the user gives a number greater than 1.
i=2  #Initializing the first number to be checked as a factor.
while i<=int(i/2)+1:  #Till which all numbers are to be checked.
    if Num%i==0:  #When a factor is encountered, the remainder is zero.
        print("Not Prime.")
        break  #No need to check the remaining numbers if the number has already been proven not prime.
    i+=1  #Increasing by one to check the next numbers if it is a factor or not.
else:
    print("Prime.")
