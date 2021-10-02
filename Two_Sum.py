class Solution:
    def twoSum(self, nums, target):
        visited = {}

        for index, num in enumerate(nums):
            second = target-num

            if second in visited:
                return[visited[second], index]
            else:
                visited[num] = index
        return []  