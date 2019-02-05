def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
# nums = [-1,-100,3,99]
# k = 2
# nums = nums[-k:] + nums[:-k]
# print(nums)
n = 5
m = 6

l = [[ i * j for j in range(m)] for i in range(n)]

for i in l:
    print('')
    for j in i:
        print(j, end=' ')
