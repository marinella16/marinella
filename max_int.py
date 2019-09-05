num_int = int(input("Input a number: "))   

max_int = 0
count = 0

#While integer is positive
while num_int >= 0:
    #Find maximum integer
    if num_int > max_int:
        max_int = num_int

    count += 1
    num_int = int(input("Input a number: "))

if count >= 0:
    print("The maximum is", max_int)  