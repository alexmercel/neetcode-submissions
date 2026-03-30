class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(nums, target):
            nums.sort()
            right=len(nums)-1
            left=0
            print(nums,target)
            op=[]
            while left<right:
                s=nums[left]+nums[right]
                if s == target:
                    b=[-target]+ [nums[right],nums[left]]
                    left +=1
                    right-=1
                    b.sort()
                    op.append(b)
                elif s<target:
                    left+=1
                elif s>target:
                    right-=1
            return op

        op=[]
        for i in range (len(nums)):
            x=nums[i]
            y=twosum(nums[0:i]+nums[i+1:],-x)
            for z in y:
                if z not in op:
                    op.append(z)     
        return op