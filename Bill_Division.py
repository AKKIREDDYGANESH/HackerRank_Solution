#Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.


def BillDivision(bill,k,b):
    bill.remove(bill[k])
    total = int(sum(bill)/2)
    remaining = b - total
    
    if remaining == 0 :
        return "Bon Appetit"
    else:
        return remaining




n = 4
k = 1
bill = [3,10,2,9]
b = 7
print(BillDivision(bill,k,b))