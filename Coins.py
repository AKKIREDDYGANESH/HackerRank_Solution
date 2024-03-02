#Maximum number of coins requies to for a given number.
def Max_coin(num):
    one = 0
    two = 0
    five = (num - 4)//5
    
    if(((num - 5*five) % 2)==0):
        one = 2
    else:
        one = 1
    
    two = (num - 5 * five - one)//2
    
    print(one+two+five)
    print(five)
    print(two)
    print(one)



num = int(input("Enter the number: "))
Max_coin(num)