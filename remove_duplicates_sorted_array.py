def removeDuplicates(nums):
    result = []
    for i, j in enumerate(nums):
        if i != j:
            result.append(i)
    return result