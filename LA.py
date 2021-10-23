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


