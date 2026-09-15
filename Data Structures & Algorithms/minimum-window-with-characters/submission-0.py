class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        if not s or not t:
            return ""

        freq_t = {}
        window_freq = {}

        left = 0
        right = 0

        formed = 0
        min_len = float("inf")
        best_start = 0

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        required_type = len(freq_t)

        while right < len(s):
            current_char = s[right]

            window_freq[current_char] = window_freq.get(current_char, 0) + 1

            if (
                current_char in freq_t
                and window_freq[current_char] == freq_t[current_char]
            ):
                formed += 1

            right += 1

            while formed == required_type:
                current_window = right - left

                if current_window < min_len:
                    min_len = current_window
                    best_start = left

                left_char = s[left]
                window_freq[left_char] -= 1

                if (
                    left_char in freq_t
                    and window_freq[left_char] < freq_t[left_char]
                ):
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[best_start:best_start + min_len]

