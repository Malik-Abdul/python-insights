# https://leetcode.com/problems/top-k-frequent-elements/submissions/1480189105/
# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        most_common = counter.most_common(k)
        most_common_keys = []
        for item in most_common:
            most_common_keys.append(item[0])
        return most_common_keys
        
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))