#Given a sequence of  integers,  where each element is distinct and satisfies . For each  where , that is  increments from  to , find any integer  such that  and keep a history of the values of  in a return array.

def solve(arr):
    new_arr = []
    for i in range(len(arr)):
        first_value = arr.index(i+1) 
        second_value = arr.index(first_value+1) 
        new_arr.append(second_value+1)
    
    return new_arr


arr = [4,3,5,1,2]
print(solve(arr))