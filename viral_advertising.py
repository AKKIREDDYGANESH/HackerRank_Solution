#HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly  people on social media.

#On the first day, half of those  people (i.e., ) like the advertisement and each shares it with  of their friends. At the beginning of the second day,  people receive the advertisement.

#Each day,  of the recipients like the advertisement and will share it with  friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day .


def solveit(n):
    shared = 5
    liked = cumulative= 0
    for i  in range(1,n+1):
        liked = int(shared/2)
        cumulative += liked
        shared = liked * 3
        
    return cumulative



n = 3
print(solveit(n))