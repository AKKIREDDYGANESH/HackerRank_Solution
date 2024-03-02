'''An integer  is a divisor of an integer  if the remainder of .

Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.'''




def findDigits(n):
    # Write your code here
    i = 0
    temp = n
    while n>0:
        rem = n%10
        if rem != 0 and temp%rem==0:
            i +=1
        n = int(n/10)
    
    return i


a = 1012
print(findDigits(a))