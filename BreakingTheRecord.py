def breakingRecords(scores,n):
    mini = 0
    maxi = 0
    arr = [scores[0],scores[0]]
    for i in range(1,n):
        if scores[i]<arr[0]:
            arr[0]= scores[i]
            mini +=1
        
        elif scores[i]>arr[1]:
            arr[1]= scores[i]
            maxi +=1
        
    print(maxi,mini)
        




n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores,n)