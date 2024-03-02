"""The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after  growth cycles?

For example, if the number of growth cycles is , the calculations are as follows:"""


def UptonTree(n):
    tall = 1
    for i in range(1,n+1):
        if i&1 == 1:
            tall = tall*2
        else:
            tall = tall+1
    return tall


n = 4
print(UptonTree(n))