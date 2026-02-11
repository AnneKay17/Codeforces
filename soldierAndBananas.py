def borrowed() -> int:
    values = input()
    values = values.split()
    k = int(values[0]) #cost of 1st banana
    w = int(values[1]) #initial dollars 
    n = int(values[2]) #number of bananas
    totalCost = 0

    for i in range(1,n+1):
        totalCost += i*k
    
    borrow = totalCost - w
    if borrow <= 0:
        return 0
    return borrow
print(borrowed())