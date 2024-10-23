'''
Question for Strings: 
Ques) Write a program to convert an integer to another number whose base is 
      given by the user. Also write a program to convert the number of base 
      given by the user back to integer.
'''
Num=int(input("Enter a positive number: "))  #Taking a whole number from user which will be converted into another number.
base=int(input("Enter the base number from 2 to 35 both inclusive: "))  #After digit 9, if we take all alphabets from A to Z, we can show a base of 35 using numbers and alphabets.
str1="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #String of all bases such that string position is the highest value of a bit of that base. For example: F is the highest value for a bit in base 16.
value=""
x=Num  #Creating another variable so that no changes are made to the original variable containing number.
while x!=0:  #If you know that to get the different base value, a number is repeatedly divided by the base number till the quotient becomes 0.
    value=str1[x%base]+value  #We are adding the remainder to the beginning of value.
    x//=base  #We are making the temporary variable equal to the quotient when the variable is divided by the base number.
print("When we convert",Num,"to the base",base,": ",value)

Str=input("Enter the value: ")  #String to be converted back to integer.
base=int(input("Enter the valid base number of the given number: "))  #Getting base number of the given number.
Str=Str.upper()  #Converting the string to uppercase since all Alphabets should be captial.
for i in Str:  #Iterating the string.
    if str1.index(i)>=base:  #Checking since a number can't be greater than it's base. For example for base 10, 9 is the highest value.
        print("Invalid value or base.")
        break  #No need to check other bits since they are invalid.
else:
    value=0  #Initializing the value which is an integer.
    for i in range(len(Str)):  #Iterating through the positions of all characters in the string given by the user.
        value+=str1.index(Str[i].upper())*base**(len(Str)-i-1)  #Basically traversing through the string using its index and adding their value calculated by their positional value multiplied by their weight which is a power of the base.
    print("The integral value is:",value)
