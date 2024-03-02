def countApplesAndOranges(s, t, a, b, apples, oranges):
    applecount = 0
    orangecount = 0
    c = []
    d = []
    for i in range(m):
        value = a  + apples[i]
        c.append(value)
    
    for j in range(n):
        value1 = b  + oranges[j]
        d.append(value1)
  
    
    for k in c:
        if k>= s and k<=t:
            applecount += 1
    print(applecount)
    
    for l in d:
        if l>=s and l<=t:
            orangecount +=1
    print(orangecount)
    
        
    







s=7
t=11
a=5
b=15
m=3
n=2
apples = [2,-2,1]
oranges = [5,-6]
countApplesAndOranges(s, t, a, b, apples, oranges)

"""first_multiple_input = input().rstrip().split()

s = int(first_multiple_input[0])

t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

a = int(second_multiple_input[0])

b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()

m = int(third_multiple_input[0])

n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)"""
