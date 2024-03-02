#This is Angry Professor problem . there is 3 inputs n,arr and k . It return the YES or No 

def Find_Time(arr,k):
    count = 0
    for i in range(len(arr)):
        if arr[i]<= 0:
            count +=1
    if count >= k:
        return "NO"
    else:
        return "YES"
    
n = 4
arr = [0,-1,2,1]
k = 2
print(Find_Time(arr,k))