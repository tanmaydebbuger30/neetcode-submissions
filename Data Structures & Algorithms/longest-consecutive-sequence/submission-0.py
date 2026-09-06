class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_seq = 0
        seen = set(nums)

        for num in seen:

            if num - 1 not in seen:
                current_num  = num
                current_length = 1
            
                while current_num + 1 in seen:
                    current_num+=1
                    current_length +=1
                max_seq = max(max_seq, current_length)


        return max_seq