from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()         # stores indices, values are in decreasing order
        res = []

        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window (i - k + 1 .. i)
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Maintain decreasing order: remove smaller/equal values from the back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Once we've formed the first window, record max (front of deque)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res