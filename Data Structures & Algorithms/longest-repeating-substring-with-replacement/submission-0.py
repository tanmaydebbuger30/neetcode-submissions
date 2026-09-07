class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        right =0
        max_freq = 0
        max_length = 0

        freq = {}

        while right < len(s):

            if s[right] not in freq:

                freq[s[right]] = freq.get(s[right], 0) + 1

            else: 
                freq[s[right]] += 1

            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -=1
                left+=1

            current_len = right - left + 1
            max_length = max(max_length, current_len)
            right+=1

        return max_length


        
