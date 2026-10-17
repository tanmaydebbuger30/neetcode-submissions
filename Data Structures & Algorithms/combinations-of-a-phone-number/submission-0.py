class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        combination = []


        mapping = {
            "2" : "abc",
            "3": "def",
            "4": "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"

        }

        def backtracking(index, current_combination):

            if index == len(digits):
                combination.append(current_combination)
                return

            current_digit = digits[index]
            element = mapping.get(current_digit)
            for words in element:
                backtracking(index + 1, current_combination + words)

        backtracking(0, "")





        return combination

        