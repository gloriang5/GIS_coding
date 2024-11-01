List = [5, 10, 15, 20, 25]
NewList = []

for i in range(len(List)):
    if i == 0 or i == (len(List) - 1):
        NewList.append(List[i])

print(NewList)
