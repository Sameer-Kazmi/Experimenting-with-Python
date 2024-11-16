'''
Ques) Write a Python program that takes user input for students' subject preferences, 
stores them in sets, and then filters students based on specified liked and disliked subjects.
'''
# Firstly, we need to ask the user the number of students who like that particular subject and 
# names of the student for all the five subjects. 
phy_num=int(input("Enter the number of students who like Physics: "))  # Taking the number of students who like Physics.
phy=set()  # Creating an empty set to store the names of the students who like Physics.
for count in range(phy_num):  # Doing a for loop so that we can ask the user for the names of the student.
    name=input("Enter the name: ")  # Asking the name of the student.
    phy.add(name)  # Adding that name to the set.
# Similarly, we need to do the same for the remaining four subjects.
chem_num=int(input("Enter the number of students who like Chemistry: "))
chem=set()
for count in range(chem_num):
    name=input("Enter the name: ")
    chem.add(name)
mat_num=int(input("Enter the number of students who like Mathematics: "))
mat=set()
for count in range(mat_num):
    name=input("Enter the name: ")
    mat.add(name)
cs_num=int(input("Enter the number of students who like Computer Science: "))
cs=set()
for count in range(cs_num):
    name=input("Enter the name: ")
    cs.add(name)
eng_num=int(input("Enter the number of students who like English: "))
eng=set()
for count in range(eng_num):
    name=input("Enter the name: ")
    eng.add(name)
univ_set=phy|chem|mat|cs|eng  # We will need a universal set containing the names of all the students.
set_user=set()  # We are initializing a set which will store the names of the desired students which will be given as output.
like_list=eval(input("Enter the list of subjects the students should like: "))  # Asking the user for a list of subjects which the student should like.
dislike_list=eval(input("Enter the list of subjects the students should dislike: "))  # Asking the user for a list of subject which the student should dislike.
mydict={"Physics":phy,"Chemistry":chem,"Mathematics":mat,"Computer Science":cs,"English":eng}  # Creating a dictionary with subject name, subject set as key,value pair.
for subject in like_list:  # Doing a for loop in the list of subjects the student should like.
    if len(set_user)==0:  # We are checking whether the set which will store the desired names is empty or not.
        set_user=mydict[subject]   # We are assigning the storing set the value of set of first desired subject. This is because we can't
                                   # perform operations on an empty set.
    else:
        set_user&=mydict[subject]  # Taking the intersection of the storing set with other liked subject sets.
for subject in dislike_list:  # Doing a for loop in the list of subjects the student should dislike.
    if len(set_user)==0:  # We are checking whether the set which will store the desired names is empty or not.
        set_user=(univ_set-mydict[subject])  # We are assigning the storing set the value of set of first not desired subject which is done by 
                                             # taking the difference of the universal set and the set of students liking that subject. 
                                             # Also, we can't perform operations on an empty set.
    else:
        set_user&=(univ_set-mydict[subject])  # Taking the intersection of the set containing the names of students disliking the subject.
print(set_user)
