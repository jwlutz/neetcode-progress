class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        event_horizon = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                two_sum = nums[i] + nums[j]

                if -two_sum in event_horizon:
                    list_repr = [-two_sum, nums[i], nums[j]]
                    list_repr.sort()
                    tuple_repr = tuple(list_repr)
                    output.add(tuple_repr)
            event_horizon.add(nums[i])

        return [list(o) for o in output]