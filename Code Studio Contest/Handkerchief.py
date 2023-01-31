from typing import *
from collections import Counter

def handkerChief(v: List[int]) -> int:

    v.sort()

    mydic = Counter(v)
    val = mydic.values()
    return max(val)

arr = [1,1,1,1]
print(handkerChief(arr))