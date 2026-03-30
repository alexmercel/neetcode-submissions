class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rightptr=len(numbers) -1
        leftptr=0
        while rightptr>leftptr:
            s=numbers[leftptr] + numbers[rightptr]
            print (s)
            if s==target:
                return [leftptr+1,rightptr+1]
            elif s<target:
                leftptr +=1
            elif s>target:
                rightptr -=1
            