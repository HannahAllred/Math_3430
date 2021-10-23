#Homework 03 problems continue below:

#Homework 03 problem 0:
def vector_addition(vector1, vector2):
#vector1 is stored as a list and vector2 is a list
    R=[]
    for element in range(len(vector1)):
        R.append("0")
        
#initializes an empty list for resultant vector 
        
    for i in range (len(vector1)):
        R[i] = vector1[i] + vector2[i]
        
#adds vector1 and vector2

    return R


vector1=(1,2,3)
vector2=(3,5,4)

result = vector_addition(vector1, vector2)
print(result)




#Homework 04 problems continue below:

#Homework 04 problem 1:
def absolute_realcomplex (complex):
    
    result = (((complex_a.imag)**2+(complex_a.real)**2))**(1/2)
# this function takes the square of the inaginary part of the input and adds it 
#to the square of the real part and takes the square root of the sum. 
    return result

complex_a = -4 + 5j

print(absolute_realcomplex(complex_a))

complex_a = 1+2j

#Homework 04 problem 2:
def p_norm(vector, scalar):

#This function will take a vector and find the pth norm of the vector. 
#The initial vector is stored as a list and the default value of p is 2. 
#input should be given for p but if input is empty p will default to 2. 

    p = ("input" or 2)
    
    for i in range(len(vector)):
        absolute_realcomplex(vector)
        
#This takes the absolute value of each element of vector. 

    for i in range(len(vector)):
        vector[i] = vector[i]**p 
        
#This takes each element of vector and raises it to the pth power. 

    inter = sum(vector)
    
#This adds the elements of vector.

    result = (inter)**(1/2)
    
#This takes the pth root of the sum of the elements of vector. 


#Homework 04 problem 3:
def inf_norm(vector):
    
#This function will take a vector and find the infinity norm of the vector. 
#The initial vector is stored as a list.

    Q = [] 

    for i in range(len(vector)):
        Q.append ("0")
        
    for i in range(len(vector)):
        Q.append (abs(i))
    
#This takes the absolute value of each element of vector. 
        
    
    result = max(Q)
#This evaluates each element of vector and determines which is the greatest.

#The greatest element of vector is the infinity norm. 



#Homework 04 problem 4:

def p_inf_bool(vector):

    bool = ("boolean" or "false")

    if bool = true:
        result = inf_norm(vector)
    
    if bool = false:
        result = p_norm(vector)
        
    return result
    
print ("result")

#This function will check a boolean value for true/false input:
#False is the default input of the boolean value. 
#If false, function will use p_norm(vector) to find the p norm of the vector. The same default input remains. 
#If true, the function will use inf_norm(vector) to find the infinity norm of the vector. 


#Homework 04 problem 5:
def inner_prod(vector_a,vector_b):

#This function should take two vectors stored as lists and find the dot product. The vectors can have both real and complex elements. 

    Q=[]
#This makes an empty list for the intermediate list that comes from multiplying each element to the corresponding element in vector_b. 

    for element in range(len(vector_a)):
        Q.append("0")

#This makes the intermediate list the appropriate legnth. 

    for i in range(len(vector_a)):
    Q[i] = (vector_a[i]*vector_b[i])
        result = vector_a[i]*vector_b[i]

#This multiplies each element by the corresponding element in vector_b. 

    result = sum(Q)
    
    return result

#This takes the sum of the intermediate list, which is the inner product. 

print ("result"):




