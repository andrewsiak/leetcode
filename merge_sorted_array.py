def merge(nums1, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    

    # compare nums1 position to nums2 position 
    # if nums1[i] is greater than nums2[i],
    # if nums1[i] is equal to nums2[i], 
    # if nums1[i] is less than nums2[i],

    # if it is less 
    nums1 = nums1 + nums2
    nums1.sort()
    print(nums1)


test1_nums1 = [1, 2, 3, 5]
test1_nums2 = [2, 4, 6]
print(merge(test1_nums1, test1_nums2))


