def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, ind = m-1, n-1, n+m-1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[ind] = nums1[i]
            i -= 1
        else:
            nums1[ind] = nums2[j]
            j -= 1
        ind -= 1

    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge(nums1, m, nums2, n))
