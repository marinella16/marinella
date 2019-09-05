

while (start < end):  
    sum= 0
    for i in range(start,end+1):
        sum += 1
        if sum - num == 0:
            for j in range(start, i+1):
                print(j, end= " "
        elif sum > num:
            print(1)
    sum = 0
    start += 1

num = int(input("Input an int: ")) # Do not change this line
start = 1
end = (num + 1) // 2

for i in range(1,num+1
    sum +=1
    if sum == num



    >>> x = input("Please input an integer: ")
Please input an integer: 5
>>> x = int(x)
>>>
>>> for i in range(1, x+1):
...     nums = range(1, i+1)
...     print(' + '.join(map(str, nums)), '=', sum(nums))



sum = 0
for i in range(1,num+1):
    sum = sum + i
    if sum == num:
        for j in range(1,num+1):
            print(j, end=" ")
    if sum > num:
        break 
num = int(input("Input an int: ")) # Do not change this line
for i in range(1,num+1):
    sum=0
    for j in range(1,num+1):
        sum=sum+j
    print(str(sum))

top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(1,top_num+1):
    sum_of_divisors = 0
    divisor = 1
    for divisor in range(0,top_num+1):
        if top_num % divisor == 0:
            sum_of_divisors += divisor
            print(divisor)
        if top_num == sum_of_divisors:
            print(divisor)


