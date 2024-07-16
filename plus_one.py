def plusOne(digits):
    # find digit at last position 
    for i in digits[::-1]:
    # if anything but 9 +1
        if i <9:
            i += 1
        elif i == 9:
            i = 0
    # else = 0, and iterate in reverse using reversed()?
    # and apply same rule 
    # if 9 is found at position [0] then .insert() "1" at position [0]
    return 

test_case_1 = [1,2,3]
test_case_2 = [4,3,2,1]
test_case_3 = [9]

print("Test 1:", plusOne(test_case_1))
print("Test 2:", plusOne(test_case_2))
print("Test 3:", plusOne(test_case_3))
