class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1

        buckets = [[] for _ in range (len(nums)+1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for frequency in range(len(buckets)-1,0,-1):
            for num in buckets[frequency]:
                result.append(num)

            if len(result)==k:
                return list(result) 





        