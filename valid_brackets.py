def isValid(s):
    # create dict of key value of matching open/close brackets
    bracket_stack = []
    bracket_dict = {
        "(": ")",
        "{": "}",
        "[": "]"
        }

        
        
    # loop through string 
    
    for i in s:
    # find matching key: value to index at end if true 
        if i in bracket_dict:
            bracket_stack.append(i)
            print("append", bracket_stack)

        #compare to tracker and if found .pop

        elif not bracket_stack or bracket_dict[bracket_stack.pop()] != i: 
            print("pop", bracket_stack)

            return False
    return not bracket_stack
        
            # if len(bracket_stack) == 0:
            #     return False
        
      
            
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
