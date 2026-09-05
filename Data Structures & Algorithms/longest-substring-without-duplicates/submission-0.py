class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        max_length = 0
        seen  = set()

        while right < len(s):

            current_length = 0

            if s[right] not in seen:
                seen.add(s[right])
                current_length = right - left + 1
                max_length = max(current_length, max_length)
                right +=1

              
            else: 
                seen.remove(s[left])
                left+=1
                

        return max_length




        


        