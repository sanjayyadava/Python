# def substratction(x,y):
#     return(x-y)

# a=10
# b=5

# res = substratction(a,b)
# print("subtraction of ", a, " and ", b, " is ", res)


# .................................................


# def funct():
#     print("hello sanjay kumar this is time ")
    
# funct() 

# .................................................   

# def subNumber(x,y):
#     return(x-y)

# a = 90
# b = 80

# res = subNumber(a,b)

# print("substactiom a " ,a ,"and  b",b, "is",res)

# ,,,,,,,,,,,,,,,,,,,,,,,

# Python program to print first 10 prime numbers

# A function name prime is defined
# using def
# def fun(n):
#     x = 2
#     count = 0
#     while count < n:
#         for d in range(2, int(x ** 0.5) + 1):  # check divisibility only up to sqrt(x)
#             if x % d == 0:
#                 break  # if divisible, it's not prime, so break the loop
#         else:
#             print(x)  # prime number
#             count += 1
#         x += 1

# # Driver Code
# n = 10

# fun(n)

# ...............................

# def fundn(func ,arg):
#     return func(arg)

# def square(x):
#     return x **  2

# res  = fundn (square ,5)
# print(res)

# .........................

# def functiondn( *args):
#     for arg in args:
#         print(arg)
        
# functiondn(1,2,3,4,5)         


# ......................................

def fundb(**kwargs):
    for k ,val in kwargs.items():
        print(f"{k} :{val}")
        
fundb(name ="sanjay kumar ",age =30 ,city ="New york")        

                