class Solution:
    def grayCode(self, n: int) -> List[int]:
        count = 1<<n 
        tmp = [i ^ i >>1 for i in range(count)]
        return tmp