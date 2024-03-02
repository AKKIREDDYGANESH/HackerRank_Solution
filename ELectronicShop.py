#A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1


def expensive(b,k,d):
    ex = []
    for i in k:
        for j in d:
            temp = i+j
            ex.append(temp)
    z = -1
    for exp in ex:
        if exp > z and exp <= b:
            z = exp
    return z

b = 10
k = [3,1]
d = [5,2,8]
print(expensive(b,k,d))