# file name: problemSetDay2.py
name=input("What is your name?")
birthday=input("When is your birthday?")
grade=input("What is your grade?")
school=input("What school do you go to?")
favorite_subject=input("What is your favorite subject?")
job=input("What do you want to be when you grow up?")

print("So you are" + name + " born on" + birthday + " in" + grade + " grade at" + school + " with your favorite subject being" + favorite_subject + " and your dream job being" +job + ".")
print("---------------")
print("Hello " + name + "!")
print("Try a quadratic by putting in values for a, b, and c!")

import cmath

a=1
b=7
c=10

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution(s) for your inputted values are {0} and {1}.'.format(sol1,sol2))
print("You can try it again by putting new values!")
