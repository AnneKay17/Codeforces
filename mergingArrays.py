n,m = list(map(int, input().split()))
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

size1 = len(array1)
size2 = len(array2)

p1 = 0
p2 = 0


merged = []
size = min(size1,size2)
while p1<size1 and p2<size2:
    if array1[p1] <= array2[p2]:
        merged.append(array1[p1])
        p1+=1
    else:
        merged.append(array2[p2])
        p2+=1


merged.extend(array1[p1: ])
merged.extend(array2[p2:])

for num in merged:
    print(num, end=" ")






