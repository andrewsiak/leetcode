def isPalindrome(x):
    front = 0
    back = len(x)-1
    # convert int to str 
    # pop left and right 
        # need to account for odd number of items in list
    
    while front < back:
        return False
    # loop through and compare first index with last index
    # OR 
    # keep track of index position and compare
        # for efficiency should identify when we the middle is reached and stop
    front = front + 1
    back = back - 1
    
    # if they are not the same return false
    # continue loop if true 
    # if all numbers in integer have been looped through, return true
    if not x:
        return True
    
