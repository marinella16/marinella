num_int = int(input("Input a number: "))   

largest = 0
count = 0

#While integer is positive
while num_int > 0:
    #Find maximum integer
    if num_int > max_int:
        num_int = max_int

    count += 1
    num_int = int(input("Input a number: "))

if count > 0:
    print("The maximum is", max_int)  