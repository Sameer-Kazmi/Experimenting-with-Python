row1=int(input("Enter the row of the first matrix: "))
col1=int(input("Enter the column of the first matrix: "))
row2=int(input("Enter the row of the second matrix: "))
col2=int(input("Enter the column of the second matrix: "))
'''
Firstly, we need to make matrix 1 and matrix 2 by getting all the
elements from the user.
'''
mat1=[]
for i in range(row1):  # Doing a for loop in the range row1 so that we can create a list for all elements present in a row.
    l=[]  # Initialising an empty list which will contain all elements belonging to a row.
    for j in range(col1):  # Doing a for loop in the range col1 so that we can ask the user to enter the elements which will be appended in the temporary list.
        element=int(input("Enter: "))  # Asking the user for an element.
        l.append(element)  # Appending the element in this temporary list which is acting as a list of elements belonging to a single row.
    mat1.append(l)  # Appending the temporary list acting as a row to the main list which is acting as the matrix 1.
#  Printing matrix 1.
for row in mat1:
    print(row)
# Similarly will happen for the second matrix.
mat2=[]
for i in range(row2):
    l=[]
    for j in range(col2):
        element=int(input("Enter: "))
        l.append(element)
    mat2.append(l)
#  Printing matrix 2.
for row in mat2:
    print(row)
if col1!=row2:  # When the column of matrix 1 and row of matrix 2 don't have the same length, then matrix multiplication can't be performed.
    print("Matrix Multiplication not feasible.")
else:
    mat=[]  # Initialising an empty list which will be our main matrix.
    for i in range(row1):  # Doing a for loop in the range row1 because that number of rows will be there in the product of the two matrices.
        l=[]  # Initialising an empty list which will be acting as list of elements belonging to the same row which will be later appended to the main matrix.
        for j in range(col2):  # Doing a for loop in the range col2 because that number of elements are present in every row.
            val=0  # Initialising the element to zero so that we can add values to it to get the final element of the matrix product.
            for k in mat1[i]:  # Doing a for loop in the ith row of the matrix 1.
                val+=k*(mat2[mat1[i].index(k)][j])
                # Basically our aim is to multiply all elements of ith row of matrix 1 to the elements of the jth column of matrix 2 to get the element 
                # placed in the ith row jth column in the matrix product. Note: Both ith row and jth column will be having the same number of elements.
                # Using the above for loop we are getting the elements of the ith row as k.
                # To get the respective element, we are taking the element of the jth column where mat1[i].index(k) signify the column number of k.
                # This column number will be actually the row number in matrix 2 and j will represent the column number.
            l.append(val)  # Appending the element to the row list.
        mat.append(l)  # Appending the row list to the matrix.
    # Printing the matrix product.
    for row in mat:
        print(row)
