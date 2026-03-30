class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums =list(set(nums))
        nums.sort()
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        print (nums)
        long=1
        temp=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                temp+=1
                print (temp)
            else:
                if temp>long:
                    long=temp
                temp=1

    
        return max(long,temp)
        