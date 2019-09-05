#Dæmi 1
num = int(input("Input an int: "))  # Don not change this line
for i in range(1,num):
    print(i)

#Dæmi 2
num = int(input("Input an int: "))
for i in range(1,num*2,2):
    print(i)

#Dæmi 3
grains_sum = 0
grains = 1
for square in range(1,65):
    grains_sum += grains
    grains*= 2

print(grains_sum)

#Dæmi 4
m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for i in range(1,n+1):
    if m % i == 0 and n % i == 0:
        gcd = i
    
print(gcd)

#Dæmi 6
top_num = int(input("Upper number for the range: "))
sum_of_divisor = 0
perfect_num = 0

for x in range(1, top_num):
        for i in range(1,x):
                if x % i == 0:
                        sum_of_divisor += i
        if x == sum_of_divisor:
                print(x)
        sum_of_divisor = 0
