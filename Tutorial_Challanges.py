def TutorialChallange(V,arr):
    return arr.index(V)


V = int(input())
n = int(input())
arr = []
for i in range(n):
    ar = int(input())
    arr.append(ar)

print(TutorialChallange(V,arr))