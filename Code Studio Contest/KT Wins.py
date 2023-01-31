from typing import *


def whoWins(T: str):
    K = 0
    L = 0

    for i in T:
        if int(i) % 2 == 0:
            K += 1
        else:
            L += 1
    if K > L:
        return "K"
    elif L > K:
        return "T"
    return "D"




whoWins('12345')



