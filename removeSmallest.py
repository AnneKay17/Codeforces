def removeSmallest():
    t = int(input())
    results = []
    while t>0:
        t-=1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        differences = []

        for i in range(len(a)-1):
            currValue = a[i]
            nextValue = a[i+1]

            diff = abs(currValue - nextValue)
            if diff <= 1:
                differences.append(diff)
        if len(a)-1 == len(differences):
            results.append("YES")
            differences.clear()
        else:
            results.append("NO")
            differences.clear()
    for res in results:
        print(res)
removeSmallest()
            
