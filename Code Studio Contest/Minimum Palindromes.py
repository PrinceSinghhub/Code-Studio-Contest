'''
   Time Complexity: O(N)
   Space Complexity: O(1)

   where 'N' is the length of the string 'S'.
'''
from typing import *

def minimumPalindromes(n: int, s: str) -> int:

    # The array 'f' stores the frequency of each character.
    f = [0 for _ in range(26)]

    # Iterate over all the characters.
    for c in s:

        # Increase the frequency of character by 1.
        f[ord(c) - ord('a')] += 1

    # 'cnt' stores the number of characters which have odd frequency.
    cnt = 0

    # Iterate over all the characters possible.
    for i in range(0, 26):

        # If the frequency is odd.
        if (f[i] % 2) != 0:

            # Increment 'cnt' by 1.
            cnt += 1

    if (cnt > (n - cnt) // 2):

        # Impossible to form the strings. Hence, return -1.
        return -1

    # If all the characters are of even frequency.
    if cnt == 0:

        # We need at least 1 string to keep all the even characters.
        return 1

    # Return the frequency of odd characters.
    return cnt
