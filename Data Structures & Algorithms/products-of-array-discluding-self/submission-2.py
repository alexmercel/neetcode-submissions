class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodsf=[1]
        pf=1
        prodsb=[1]
        pb=1
        for i in range(len(nums)-1):
            pf*=nums[i]
            pb*=nums[-i-1]
            prodsf.append(pf)
            prodsb.append(pb)
        prodsb.reverse()
        ans=[]
        for i in range(len(prodsf)):
            ans.append(prodsf[i]*prodsb[i])
        return ans
