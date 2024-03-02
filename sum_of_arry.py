def sum_arry(arr):
    a=sum(arr)
    return a





n=int(input("Enter the number of values: "))
arr=list(map(int,input("enter the arry values: ").strip().split()))
result= sum_arry(arr)
print(arr)
print(result)