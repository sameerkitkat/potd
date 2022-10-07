def intersection(nums1, nums2):
    n, m = len(nums1)-1, len(nums2)-1
    i, j = 0, 0
    res=[]
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    # [1,1,2,2] [2,2]

    while i <= n and j <= m:
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] < nums2[j]:
            i+=1
        else:
            j+=1

    return res


if __name__ == '__main__':
    nums1 = [7,2,2,4,7,0,3,4,5]
    nums2 = [3,9,8,6,1,9]
    print(intersection(nums1, nums2))
