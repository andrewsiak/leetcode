def isPalindrome(x):
    # create empty string variable
    x_string = str(x)
    #loop through string
    for i in x_string:
        if i.isalnum():
            x_string += i.lower()
    if x_string != x_string[::-1]:
        return False
    else:
        return True




test_case_one = 121
print("Case 1 :", isPalindrome(test_case_one))

test_case_two = -121
print("Case 2 :", isPalindrome(test_case_two))

test_case_three = 10
print("Case 3 :", isPalindrome(test_case_three))

test_case_four = 121121
print("Case 4 :", isPalindrome(test_case_four))

test_case_five = 123454321
print("Case 5 :", isPalindrome(test_case_five))

# below are notes from hackbright course instructor solution:
    # convert int to str 
    # pop left and right 
        # need to account for odd number of items in list
    
    # loop through and compare first index with last index
    
    # OR 
    # keep track of index position and compare
        # for efficiency should identify when we the middle is reached and stop
        
    
    # if they are not the same return false
    # continue loop if true 
    # if all numbers in integer have been looped through, return true
    
    
    
    
    
    # alternate solution incomplete, instead of iterating through the whole string, directly compare front and back of string, need to resolve positive comparisons
    # front = 0
    # back = len(x)-1
    # while front < back:

    #     if x[front] != x[back]:
    #         return False
    #     front = front + 1
    #     back = back - 1 if not x:
    #     return True
    
