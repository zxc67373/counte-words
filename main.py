class Solution:
    def largestSumAfterKNegations(, nums: List[int], k: int) -> int:
        nums.sort()
        b = []
        a = []
        flag_0 = 0
        for i in range(len(nums)):  # 排序 输出负数数组
            if nums[i] < 0:
                b.append(nums[i])
            if nums[i] == 0:
                flag_0 = 1
            if nums[i] > 0:
                a.append(nums[i])  # 正数组
        coutsum = 0

        if k >= len(b):
            if flag_0 == 1:
                return (-sum(b)) + sum(a)

            elif (k%2!=0 and len(b)%2==0) or (k%2==0 and len(b)%2!=0):
                if len(b) == 0 :
                    return sum(nums) - 2*min(nums)
                if len(a) == 0:
                    return -sum(nums)+2*max(nums)
                elif abs(max(b)) < min(a):
                    return (-sum(b)) + sum(a) - 2*abs(max(b))
                else:
                    return (-sum(b)) + sum(a) - 2*min(a)

            else :
                if len(b) == 0:
                    return sum(nums)
                else:
                    return (-sum(b)) + sum(a)


        else:
            for i in range(k):
                coutsum = -b[i] + coutsum
            result = 2 * coutsum + sum(b)
            return result + sum(a)

