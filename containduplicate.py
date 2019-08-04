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

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if n in dic: return True
            dic[n] = 1
        return False
查找list中是否存在duplicate
查找的例子都可以使用hash表降低时间复杂度
'''
