def isValid(s):
    parenthesis = 0
    # create dict of key value of matching open/close brackets
    for i in s:
        if i == "(":
            parenthesis += 1
        elif i == ")":
            parenthesis -= 1
            if parenthesis == 0:
                print(parenthesis)
                return True
            elif parenthesis != 0:
                print(parenthesis)
                return False
            
    # loop through string 
     

    # find matching key: value to index at end if true 
    
    

test_1 = "()"
print("Case 1:", isValid(test_1))

test_2 = "()[]{}"
print("Case 2:", isValid(test_2))

test_3 = "(]"
print("Case 3:", isValid(test_3))
