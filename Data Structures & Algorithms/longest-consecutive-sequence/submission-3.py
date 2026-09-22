class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq=1
        l=len(nums)
        if l == 0:
            return 0
        elif l==1:
            return 1
        nums=sorted(set(nums))
        print(nums)
        c=1
        for i in range (1,len(nums)):
            if nums[i]==nums[i-1]+1:
                c+=1
                seq=max(seq,c)
            else: 
                c=1
        return seq
        