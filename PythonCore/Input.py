# Python program showing 
# a use of input()

val = input("Enter your value: ")
print(val)


for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)