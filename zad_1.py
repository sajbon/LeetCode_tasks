nums = [2, 7, 11, 15]
target = 9


class Solution(object):
    def twoSum(self, nums, target):
        for index1 in range(0, len(nums)):
            for index2 in range(0, len(nums)):
                if nums[index1] + nums[index2] == target and index1 != index2:
                    solution = index2, index1
        return solution


solution_instance = Solution()
print(solution_instance.twoSum(nums, target))
