'''
Write a Python program to rank the top 3 students based on their marks, taking the 
number of students and their names, marks as user input, using dictionaries.
'''
dict1={}  # Creating a dictionary to store name,marks as key,value pair.
num=int(input("Enter the number of students: "))  # Taking the number of students as input.
for count in range(num):  # Doing a for loop to ask the user n number of times name and marks which will be stored in the dictionary.
    Name=input("Enter the student's name: ")
    Marks=float(input("Enter the student's marks: "))
    dict1[Name]=Marks
dict2={"First":["",0],"Second":["",0],"Third":["",0]}  # Creating a dictionary where the position is the key and a list of name, marks will be the value.
for Name,Marks in dict1.items():  # Iterating the dictionary containing name,marks pair using dict_name.items().
    if Marks>dict2["First"][1]:  # When the marks of the student is greater than the marks of the student in the dictionary who is in first position.
        dict2["Third"]=dict2["Second"]   # The student who was earlier in second position, will be now in the third position.
        dict2["Second"]=dict2["First"]  # The student who was earlier in first position, will be now in the second position.
        dict2["First"]=[Name,Marks]  # The student whose name is in the loop will be in the first position.
    elif Marks>dict2["Second"][1]:  # When the marks of the student is greater than the marks of the student in the dictionary who is in second 
                                    # position. It is to be noted that since this condition is after the first condition, the first condition 
                                    # has to be false to arrive to the second condition. Therefore this condition's program will only run if the 
                                    # marks is lesser than first and greater than second.'''
        dict2["Third"]=dict2["Second"]  # The student who was earlier in second position, will be now in the third position.
        dict2["Second"]=[Name,Marks]  # The student whose name is in the loop will be in the second position.
    elif Marks>dict2["Third"][1]:  # When the marks of the student is greater than the marks of the student in the dictionary who is in the 
                                   # third position. It is to be noted that we will arrive to this condition only and only if the condition 
                                   # to come in first and second position comes out to be false.'''
        dict2["Third"]=[Name,Marks]  # The student whose name is in the loop will be in the third position.
# Now printing the name of the students who came first, second and third with their respective marks.
print(dict2["First"][0],"came first with",dict2["First"][1],"marks.")
print(dict2["Second"][0],"came second with",dict2["Second"][1],"marks.")
print(dict2["Third"][0],"came third with",dict2["Third"][1],"marks.")
