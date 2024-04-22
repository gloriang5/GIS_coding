def histogram(list):
    for i in list:
        stars = i
        print(i*"*")

input_list = []
n = int(input("How many layers are there in the histogram? "))
for i in range(n):
    num = int(input(f"Enter the number of units in {i+1} layer: "))
    input_list.append(num)

histogram(input_list)

