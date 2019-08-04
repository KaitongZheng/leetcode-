class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return 'true'
        return 'false'
a=[1,2,3,4]
b= Solution()
c=b.containsDuplicate(a)
print(a)
print(c)
