#Question 1
m_str = input('Input m: ')  # do not change this line
m_str = float(m_str)# change m_str to a float
c = 300000000# remember you need c
e = m_str * c **2# e = 
print("e =", e)  # do not change this line

#Question 2
in_str = input("Input s: ")
in_int = int(in_str)# in_int =
print("in_int = ", in_int)
in_float = float(in_str)# in_float =
print("in_float = ", in_float)


#Question 3
import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)# convert strings to ints
d = math.sqrt((x2_int - x1_int)**2 + (y2_int - y1_int)**2)#  d =
print("d =",d)  # do not change this line


#Question 4
weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line
weight_float= float(weight_str)
height_float = float(height_str)/100
bmi = weight_float / (height_float**2)
print("BMI is: ", bmi) # do not change this line


#Question 5
x_str = input("Input x: ")
x_str = int(x_str)# remember to convert to an int
first_three= int(x_str//1000)# first_three =
last_two = int(x_str%100)# last_two =
middle_two = int(x_str//100)%100# middle_two =
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)


#Question 6
secs_str = input("Input seconds: ") # do not change this line
secs_int=int(secs_str)
seconds=secs_int%(24*3600)
# hours =
hours = seconds //3600
seconds%=3600
# minutes =
minutes=seconds//60
# seconds =
seconds %=60
print(hours,":",minutes,":",seconds) # do not change this line
