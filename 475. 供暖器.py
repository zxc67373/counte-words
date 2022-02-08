class Solution:
    def binarySearch(nums, target):
        left = 0
        right = len(nums) - 1
        if nums[left] > target:
            return -1
        while (left < right):
            mid = int((right - left + 1) / 2) + left
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left

    def findRadius(, houses: list[int], heaters: list[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            i = Solution.binarySearch(heaters, house)
            j = i + 1
            leftdistence = float('inf') if i < 0 else house - heaters[i]
            rightdistence = float('inf') if j >= len(heaters) else heaters[j] - house
            curdistence = min(leftdistence, rightdistence)
            ans =max(ans, curdistence)
        return ans


houses = [1, 2, 3]
heaters = [2]
Solution.findRadius(houses=houses,heaters=heaters)