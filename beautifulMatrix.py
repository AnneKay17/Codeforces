n = 5
matrix = []
while n > 0 :
    numbers = input()
    values = numbers.split()
    matrix.append(values)
    n-=1

targetarray = matrix.index(matrix[2])
targetPoint = matrix[2]
for array in matrix:
    if "1" in array:
        arrayIndex = matrix.index(array)
        oneIndex = array.index("1")
        distanceX = abs(oneIndex - 2)
        distanceY= abs(arrayIndex - 2)
        total = distanceX + distanceY
        

        
        print(total)
