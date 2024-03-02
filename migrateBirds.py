#Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
def solve(num):
   
    return max(set(num),key=num.count)



n = 11
num = [1,2,3,4,5,4,3,2,1,3,4]
print(solve(num))