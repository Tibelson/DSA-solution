class Solution:
    def hammingWeight(self, n: int) -> int:
        res  = list(bin(n))
        return res.count('1')
        # count = 0
        # for num in res:
        #     if num == 1:
        #         count += 1
        # return count

