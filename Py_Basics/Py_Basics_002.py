
# Python Input Output

name = input("Enter your name :")
print('Your name is : '+name)


# Print conditional Input from User

age_input = input("Enter your Age : ")
age = int(age_input)

if age<18:
   print('You are not adult')

elif age>=18 and age<=29:
    print('You are adult')

elif age>=30 and age<=45:
    print('You are youngster')

else:
    print('You are senior citizen')



# Nested If Else Statements

age = 70
is_member = True

if age >= 18:
   if is_member:
       print('30% discount')
   else:
        print('10% discount')
else:
    print('No discount')