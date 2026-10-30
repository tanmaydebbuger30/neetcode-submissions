class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        current_state = []
        subsets = []
        index = 0

        def backtracking(index, current_state):
            # base case when index reaches till the end of the nums
            if index == len(nums):
                # copy the current_state and save it subsets
                current_subset = current_state.copy()
                subsets.append(current_subset)
                return 

            # include the next number is the list   
            current_state.append(nums[index])
            backtracking(index+1, current_state)
            current_state.pop()
            backtracking(index+1, current_state)
        backtracking(0, current_state)
        return subsets




        

         
        