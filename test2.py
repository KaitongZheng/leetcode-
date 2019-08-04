class Solution:
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] =1
        print(hash_table)
        return hash_table.popitem()[0]
a=Solution()
b=[1,1,1,1,2,2,4,3,3,3]
c={}
print(a.singleNumber(b))
