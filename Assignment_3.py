#Dæmi 1
num = int(input("Input an int: ")) # Do not change this line
x_int = 1
while x_int < num:
    print(x_int)
    x_int = x_int + 1


#Dæmi 2
num = int(input("Input an int: ")) # Do not change this line
counter = 1
num = num * 2

while counter < num:
    print (counter)
    counter += 2


#Dæmi 3
total=0
num = 0
    
while num != 10:
    total = total + num
    num = int(input("Input an int: "))
print (total)


#Dæmi 4
n = int(input("Input an int: ")) # Do not change this line
value = 1
while value <= n:
    if(n%value == 0):
        print(value)
    value = value + 1


#Dæmi 5
n = int(input("Input a natural number: ")) # Do not change this line

count = 0
i = 2

while(i <= n//2):
    if (n % i == 0):
        count = count + 1
        break
    i = i + 1

prime = (count == 0 and n != 1)

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")

#Dæmi 6
AB = 10

while True:
    CAB = AB ** 2
    two_digits = CAB % 100
    if two_digits == AB:
        print(AB)
        break
    AB += 1

#/eða Dæmi 6
num = 10
while num < 100: # Check to see if its a two digit number
    num2 = num * num 
    if num2 < 1000: # Check to see if its a three digit number and not above
        num3 = num2%100 # Remove all digits above 2 digits
        if num3 == num: # Compare original and final number
            print(num3)
        num+=1

#Dæmi 7
hole = 1
while hole <= 18:
    par = int((input("Par of hole " + str(hole)+": " )))
    score = int((input("Score on hole " + str(hole)+ ": " )))

    if par - score > 3:
        print("invalid score")
    elif par - score == 3:
        print("albatross")
    elif par - score ==2:
        print ("eagle")
    elif par - score == 1:
        print ("birdie")
    elif score == par:
        print ("par")
    elif score - par == 1:
        print("bogey")
    elif score - par == 2:
        print ("double bogey")
    elif score - par == 3:
        print ("triple bogey")
    else:
        print("bad hole")
    hole = hole + 1