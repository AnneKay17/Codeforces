n,m = list(map(int, input().split()))
array1= list(map(int, input().split()))
array2 =list(map(int, input().split()))

p1 = 0 
count = 0

array =[]
for p2 in range(len(array2)):
    while p1 < len(array1):
        if array1[p1] < array2[p2]:
            count+=1
            p1+=1
        else:
            break
    array.append(count)
      
for i in array:
    print(i, end =" ")