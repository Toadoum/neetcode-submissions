
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        final = []

        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1

        for key, val in res.items():
            final.append((key, val))

        final.sort(key=lambda x: x[1], reverse=True)

        return [key for key, val in final[:k]]
