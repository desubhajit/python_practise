
# This code snippets are only related to print function and avaiables

# Basic Hello World Print
print('Hello Worlds')



# Print Blank Lines
print('Hello World, this is the first line')
print(8 * '\n')
print('Hello this is the second line')



# Print the Variables
a = 10
b = 25
c = 'Hello World'
d = 'Lenovo Legion'
print(a)
print(a+b)
print(c)
print(c+d)
print(str(a)+c)


# Print Local vs Global variables

x = "First Value"
print(x)

def printTheValue():
 print(x)

printTheValue()


def printTheValues():
 global x
 x='Second Global Value' #This ovverrides the previous value of X from 'Local variable' to 'Global Variable'
 print(x)

printTheValues()
print(x)

