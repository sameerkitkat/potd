def sort_012(nums):
    low = 0
    high = len(nums)-1
    mid = 0

    while(mid<=high):
        if nums[mid] is 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            mid+=1
            low+=1
        elif nums[mid] == 1:
            mid+=1
        else:
            nums[high],nums[mid] = nums[mid],nums[high]
            high-=1

    print(nums)

if __name__ == "__main__":
    nums = [0,1,1,2,2,0,0,1,1,0,2,2,1,0,2]
    sort_012(nums)