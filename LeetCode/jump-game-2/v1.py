# [2,3,0,1,4]
class Solution:
    
    def jump(self, nums: List[int]) -> int:
        last_idx = len(nums)
        current_idx = 0
        current_step = 0
        min_step = 0
        for i in range(1, nums[current_idx] + 1):
            step_cost = self.jumpOne(current_idx + i, current_step + 1, nums)
            if step_cost != -1 and (step_cost < min_step or min_step == 0):
                min_step = step_cost
        return min_step
        
    def jumpOne(self, idx: int, step: int, nums: List[int]) -> int:
        if idx >= (len(nums) - 1):
            return step
        min_step = 0
        for i in range(1, nums[idx] + 1):
            step_cost = self.jumpOne(idx + i, step + 1, nums)
            if step_cost != -1 and (step_cost < min_step or min_step == 0):
                min_step = step_cost
        return min_step
        