class Solution:
    def hasDuplicate(self, nums):
        hs=set()
        for num in nums:
            if num in hs:
                return True
            hs.add(num)
        return False        





         