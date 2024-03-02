#In this arry we need to reurn value that count of number between two value that is X and Y . we should return minnimun count of the values



arr = [3,2,5,7,0,1,4,7,6]
x= 5
y= 7
index = []
count =[]
for i in range(len(arr)):
    if arr[i]==x:
        index.append(i)
    if arr[i]==y:
        index.append(i)
        

#[1,5,8]
value1 = arr[index[0]:index[1]+1]

first = len(value1)-2
count.append(first)

value2 = arr[index[1]:index[2]+1]
sec = len(value2)-2
count.append(sec)

print(min(count))