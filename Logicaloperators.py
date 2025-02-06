# Python Logical Operators

# Logical AND operator Examples


# a = 10
# b = 12
# c = 0
# if a and b and c:
#     print("All the numbers have boolean value as True")
# else:
#     print("Atleast one number has boolean value as False")



# Example: Logical Operators (AND, OR, NOT) with generic variables
# a, b, c = True, False, True

# # AND: Both conditions must be True
# if a and c:
#     print("Both a and c are True (AND condition).")

# # OR: At least one condition must be True
# if b or c:
#     print("Either b or c is True (OR condition).")

# # NOT: Reverses the condition
# if not b:
#     print("b is False (NOT condition).")

# a = 10
# b = 10
# c = -10

# if a > 0 and b > 0:
#     print(" The number are greater than 0 ")
 
# if a > 0 and b > 0 and c > 0 :
#     print("The number are greater than 0")
    
# else: 
#     print("Atleast one number is greater than 0") 


# a = 10 
# b = 12

# c = 0

# if a and b and c: 
#     print ("All the number have boolean value as true")
# else:
#     print("Atleast one number has boolean value as false ")
    
    
     # Logical OR operator in Python Examples
    
    
# a = 10
# b = -10
# c = 0
    
# if a > 0 or b > 0:
#         print("Either of the number is greater  than 0")

# else: 
#         print(" No number is greate than 0 ")
        
# if b > 0 or c > 0:
#         print("Either of the number is greater than 0")  
# else: 
#         print(" print no number is greater than 0")  
        
# a = 10
# b = 12
# c = 0
# if a or b or c :
#     print ("Atleast one number has  boolean value as true ")
# else:
#     print("All number have boolean value as false ")
   
# a = 10

# if not a :
#     print("boolean value of a is true ")
# if not (a % 3 == 0 or a % 5 ==0):
#     print("10 is not divisible of 5 or 3")
# else: 
#     print("10 is divisible by 3 or 5 ")  
        
         
def order(x):
    print("Method called for value :", x)
    return True if x > 0 else False

a = order
b = order
c = order
if a(-1) or b(5) or c(10):
    print("Atleast one of the number is positive")  




    
           