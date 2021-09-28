#adding vectors problen 0
#Problem #0
#Write an algorithm to implement vector addition. 
#Q1: What do we have?
#A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 
#Q2: What do we want?
#A2: Their sum stored as a list.
#Q3: How will we get there?
#A3: We will create an empty list of the appropriate size and store the sums of
#the corresponding components of vector_a and vector_b. 
# Initialize result as an empty list
# Add an element to result for each element of vector_a. Set that element to 0.
# Set each element of result to be equal to the desired sum.
# Return the desired result.

def add_vectors(vector_a, vector_b):
    R=[]
    
    length = len(vector_a)
    if len(vector_b) > length:
        length = len(vector_b)
    
    for element in range(length):
        R.append("0")
    
    for i in range(length):
        sum = 0
        if i < len(vector_a):
            sum += vector_a[i]
        if i < len(vector_b):
            sum += vector_b[i]
        R[i] = sum
    
    return R

#Problem #1
#Write an algorithm to implement scalar-vector multiplication.
#Q1: What do we have?
#A1: One vector stored as a list and one scalar. Names are vector_a and scalar_a. 
#Q2: What do we want?
#A2: The product of the scalar and vector stored as a new list.
#Q3: How will we get there?
#A3: First, we create an empty list of the correct size. We will multiply each term in vector_a by scalar_a and store the result in the empty list. 
#Create an empty list vector_b:[]
#Multiply term one in vector_a by scalar_a and store as term one in list
#repeat for legnth of vector_a
#return vector_b which is the product of scalar_a and vector_a. 

def  scavec_multi(vector, scalar):
    R=[]
    for element in range(len(vector)):
        R.append("0")
    
    for i in range(len(vector)):
        R[i] = vector[i]*scalar
        
    return R


#Problem #2
#Write an algorithm to implement scalar-matrix multiplication.
#Q1: What do we have?
#A1: One matrix stored as a list and one scalar. Names are matrix_a and scalar_a. 
#Q2: What do we want?
#A2: The product of the scalar and matrix stored as a new list.
#Q3: How will we get there?
#A3: First, we create an empty list of the correct size. We will multiply matrix_a by scalar_a and store the result in the empty list. 
#Create a new empty list for matrix_b: []
#Multiply the first column in matrix_a by scalar_a and store in matrix_b. 
#repeat for each column in matrix_a for the legnth of matrix_a.
#Return matrix_b which is the product of matrix_a and scalar_a. 

def scamatr_multi(matrix_a, scalar_a):
    R=[]
    lengthOfVector = len(matrix_a[0])
    
    for i in range(len(matrix_a)):
        R.append([])
        for j in range(lengthOfVector):
            R[i].append("0")
    
    for i in range(len(matrix_a)):
        for j in range(lengthOfVector):
            R[i][j] = matrix_a[i][j] * scalar_a
    
    return R


#Problem #3
#Write an algorithm to implement matrix addition.
#Q1: What do we have?
#A1: We have two matricies of the same size stored as lists. These are called matrix_a and matrix_b
#Q2: What do we want?
#A2: The sum of the two matricies stored as a new list.
#Q3: How will we get there?
#A3: First, we create an empty list of the correct size. We will add each term in matrix_a to the corresponding term in matrix_b and store 
#the result in the empty list. 
#Create an empty list matrix_c:[]
#Add each term in matrix_a to the corresponding term in matrix_b, store the sum in the corresponding place in matrix_c. 
#return matrix_c which is the sum of matrix_a and matrix_b. 

def matr_addi(matrix_a, matrix_b):
    R=[]
    lengthOfVector = len(matrix_a[0])
    
    for i in range(len(matrix_a)):
        R.append([])
        for j in range(lengthOfVector):
            R[i].append("0")
    
    for i in range(len(matrix_a)):
        for j in range(lengthOfVector):
            R[i][j] = matrix_a[i][j] + matrix_b[i][j]
    
    return R


#Problem #4

#Write an algorithm to implement matrix-vector multiplication using the linear
#combination of columns method. You must use the algorithms from Problem #0 and
#Problem #1.  
#Q1: What do we have?
#A1:We have a matrix stored as a list, matrix_a, and a vector stored as a list, vector_a. 
#Q2: What do we want?
#A2: We want the product of matrix_a and vector_a stored as a new list. 
#Q3: How will we get there?
#A3: We will use the linear combination of columns method, take the first column of matrix_a and multiply it by the first term in vector_a using 
#scavec_multi(vector_a,scalar_a). Repeat for the legnth of matrix_a and store as an intermediate group of lists, then add each column product
#until we are left with a single vector stored in our computer. 
#Create an empty list to store the resultant matrix. 
#Take the first column of matrix_a and multiply it by the first term in vector_a using our algorithm scavec_multi. Store the result in a new 
#matrix, matrix_int. 
#Repeat for each column and corresponding row in matrix_a and vector_a, until all columns are new and stored in matrix_int. 
#Take the rows of matrix_int and add them together using our algorithm add_vectors. 
#Return vector_b, the product of our original matrix and vector. 

def matrvec_lccmulti(matrix_a,vector_a):
    R=[]
    lengthOfVector = len(matrix_a[0])
    
    for i in range(len(matrix_a)):
        R.append([])
        for j in range(lengthOfVector):
            R[i].append("0")
    
    for i in range(len(matrix_a)):
        for j in range(lengthOfVector):
            R[i][j] = matrix_a[i][j] * scalar_a
    
    return R
    
def add_vectors(vector_a, vector_b):
    R=[]
    
    length = len(vector_a)
    if len(vector_b) > length:
        length = len(vector_b)
    
    for element in range(length):
        R.append("0")
    
    for i in range(length):
        sum = 0
        if i < len(vector_a):
            sum += vector_a[i]
        if i < len(vector_b):
            sum += vector_b[i]
        R[i] = sum
    
    return R    






vector_a = [4,7,21]
vector_b = [1,2]
matrix_a = [[1,2,3],[4,5,6],[7,8,9]]
matrix_b = [[9,8,7],[6,5,4],[3,2,1]]
scalar_a = 7
result = []

result = add_vectors(vector_a, vector_b)
print(result)

result = scavec_multi(vector_a, scalar_a)
print(result)

result = scamatr_multi(matrix_a, scalar_a)
print(result)

result = matr_addi(matrix_a, matrix_b)
print(result)