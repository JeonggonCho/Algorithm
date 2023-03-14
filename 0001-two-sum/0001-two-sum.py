class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_ls = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index_ls.append(i)
                    index_ls.append(j)
        return index_ls