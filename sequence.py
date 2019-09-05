#Input length of sequence
n = int(input("Enter the length of the sequence: ")) 
num1= 1
num2 = 2
num3 = 3
sequence = 0
count = 0

print(num1)
print(num2)
print(num3)
#Algorithm for sequence
while count <= n-4:
    sequence = num1 + num2 + num3
    print(sequence)
    num1 = num2
    num2 = num3
    num3 = sequence
    

    count += 1
    
