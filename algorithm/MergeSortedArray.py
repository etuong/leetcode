from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:n] = nums2
            return
        if n == 0:
            return
        a = 0
        b = 0
        firstArray = nums1[:m]
        for x in range(m + n):
            if a < m and (b >= n or firstArray[a] <= nums2[b]):
                nums1[x] = firstArray[a]
                a = a + 1
            else:
                nums1[x] = nums2[b]
                b = b + 1
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = m - 1
        b = n - 1
        c = m + n - 1
        while b >= 0:
            if 


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()