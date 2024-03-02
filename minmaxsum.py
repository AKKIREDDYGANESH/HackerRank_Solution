import math
def miniMaxSum(arr):
    # Write your code here
    sum1 = []
    for i in range(len(arr)):
        rem_ele = arr.pop(i)
        value = sum(arr)
        sum1.append(value)
        arr.insert(i,rem_ele)
        
    min_value = min(sum1)
    max_value = max(sum1)
    print(min_value,max_value)
    
   
arr = list(map(int, input("Enter arry: ").strip().split()))

miniMaxSum(arr)
