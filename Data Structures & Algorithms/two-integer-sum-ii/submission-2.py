class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = dict()
        c=0
        for i in numbers:
            if target - i in seen:
                return [seen[target - i]+1,c+1]
            seen[i] = c
            c+=1

        