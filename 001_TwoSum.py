class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _dict = dict()
        for index, value in enumerate(nums):
            if target - value in _dict:
                return [_dict[target-value] , index]
            _dict[value] = index
        return _dict