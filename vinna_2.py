first = int(input("First: "))
step = int(input("Step: "))
sum_of_series = 0

num = first
print(first, end=" ")

while sum_of_series <= 100:
    first += step
    print(first, end= " ")
    sum_of_series = sum_of_series + first

print ()
print("Sum of series: " + str(sum_of_series + num))

