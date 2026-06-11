class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = sorted(nums)
        self.k = k
        self.arr = self.stream[-k:]
        print(self.arr)

    def add(self, val: int) -> int:
        if len(self.arr)<self.k:
            self.arr.append(val)
            self.arr.sort()
            return self.arr[0]
        if val < self.arr[0]:
            return self.arr[0]
        else:
            self.arr[0] = val
            self.arr.sort()
            return self.arr[0]

