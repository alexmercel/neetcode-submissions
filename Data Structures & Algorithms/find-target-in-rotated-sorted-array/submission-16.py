class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        if len(nums) == 1 and nums[0] == target:
            return 0
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l=mid+1
                else:
                    r=r-1

            else:
                if nums[l]<=target<nums[mid]:
                    r=r-1
                else:
                    l=l+1

        return -1