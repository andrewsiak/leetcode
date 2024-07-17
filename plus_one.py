def plusOne(digits):
    # find digit at last position 
    # else = 0, and iterate in reverse using reversed()?
    # original solution below iterates through values instead of indicies
    # for i in digits[::-1]: 
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        return [1] + digits
    # if anything but 9 +1
        
    # and apply same rule 
    # if 9 is found at position [0] then .insert() "1" at position [0]

test_case_1 = [1,2,3]
test_case_2 = [4,3,2,1]
test_case_3 = [9]

print("Test 1:", plusOne(test_case_1))
print("Test 2:", plusOne(test_case_2))
print("Test 3:", plusOne(test_case_3))

def plusOnezo(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        return [1] + digits