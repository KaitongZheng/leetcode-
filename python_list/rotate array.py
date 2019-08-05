class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new=nums[:]
        for i in range(0,len(nums)):
            new[(i+k)%len(nums)]=nums[i]
##        nums=new[:]
        for i in range(0,len(nums)):
            nums[i]=new[i]
        return nums
a=[1,5,23,2,"a",4]
b= Solution()
c=b.rotate(a,3)
print(a)
print(c)
