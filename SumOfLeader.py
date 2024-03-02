#This is the sum of leader in  a arry . The condition is the value is not less than the remaining right most list in array.And return the sum of all leader


def sumof(mai,rem):
    if len(rem)> 0:
        max_value = max(rem)
        if mai > max_value:
            return mai
        else:
            return 0 
    else:
        return 0

#This sum of all arr



arr = [23,47,82,44,31,15,22,9]

sum =arr[len(arr)-1]
for i in range(len(arr)):
    mai = arr[i]
    
    rem = arr[i+1:]
    value =  sumof(mai,rem)
    
    sum += value
    
print(sum) 
        