def solve(steps,path):
    volume = 0
    count = 0
    for i in path:
        if i =="U":
            count +=1
            if count == 0:
                volume +=1
        elif i =="D":
            count -=1
    return volume




steps = 8
path = "UDDDUDUU"
print(solve(steps,path))