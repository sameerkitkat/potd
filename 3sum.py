def three_sum(nums, target):
    res = []
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        if nums[i] > target:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            two_sum(nums, i, res, target)
    return res


def two_sum(nums, idx, res, target):
    low = idx + 1
    high = len(nums) - 1

    while low < high:
        sum = nums[idx] + nums[low] + nums[high]
        if sum < target or (low > idx + 1 and nums[low] == nums[low - 1]):
            low += 1
        elif sum > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
            high -= 1
        else:
            res.append([nums[idx], nums[low], nums[high]])
            low += 1
            high -= 1


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    ans = three_sum(nums, 0)
    print(ans)
