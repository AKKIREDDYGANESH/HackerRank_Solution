#This is a beautiful days at the Movies problem
#

def SolveIt(i,j,k):
    count = 0
    for i in range(i,j):
        rev = int(str(i)[::-1])
        value = abs(i-rev)
        if value%k == 0:
            count +=1
    
    return count
    
    

i = 20
j = 23
k = 6
print(SolveIt(i,j,k))