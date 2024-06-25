def removeDuplicates(nums):
    position = 0
    for i, j in enumerate(nums[1:],1):
        if nums[i-1] != j:
            position += 1
            nums[position] = j
    return position+1


    # solution by creating array of unique nums
    # result = []
    # for i in nums:
    #     if i not in result:
    #         result.append(i)
    #         print(result)
    # return len(result)


test_1 = [1,1,2]
print(removeDuplicates(test_1))

test_2 = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(test_2))

test_3 = [1,1,3,3,5,5]
print(removeDuplicates(test_3))
