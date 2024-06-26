def isValid(s):
    # create dict of key value of matching open/close brackets
    result = 0
    bracket_dict = {
        "(": ")",
        "{": "}",
        "[": "]"}
        
        
    # loop through string 
    
    for i in s:
    # find matching key: value to index at end if true 
        if i in bracket_dict:
            result += 1
        
            if result == 0:
                print(result)
                return True
      
            
         # parenthesis = 0
    # for i in s:
    # # find matching key: value to index at end if true 
    #     if i in bracket_dict:
    #         parenthesis += 1
    #     elif i == ")":
    #         parenthesis -= 1
    #         if parenthesis == 0:
    #             print(parenthesis)
    #             return True
    #         elif parenthesis != 0:
    #             print(parenthesis)
    #             return False


    
    

test_1 = "()"
print("Case 1:", isValid(test_1))

test_2 = "()[]{}"
print("Case 2:", isValid(test_2))

test_3 = "(]"
print("Case 3:", isValid(test_3))
