class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # seq=1
        # l=len(nums)
        # if l == 0:
        #     return 0
        # elif l==1:
        #     return 1
        # nums=sorted(set(nums))
        # print(nums)
        # c=1
        # for i in range (1,len(nums)):
        #     if nums[i]==nums[i-1]+1:
        #         c+=1
        #         seq=max(seq,c)
        #     else: 
        #         c=1
        # return seq
        # a o(n) approach
        hashmap = set(nums)
        c=0
        maxc=0
        for i in nums:
            if i - 1 not in hashmap:
                counter=1
                while c<len(nums) and i+counter in hashmap:
                    counter+=1
                    c+=1
                maxc=max(maxc,counter)
        return maxc