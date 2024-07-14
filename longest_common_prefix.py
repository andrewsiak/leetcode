def longestCommonPrefix(strs):
# find letter at index 0 of index 0 str
    prefix_result = ""

    for i in range(len(strs)):
        if strs[0][i] != strs[-1][i]:
            
            # this is incorrect, placeholder for now
            return prefix_result
        prefix_result += strs[0][i]
    return prefix_result
    
    

# iterate through list of strings, and compare to index 0 of each string in list until end of list
#   or compare first of each string, if same return true, else end loop
# if letter matches in all stringssave to a variable "prefix"
# else if letter does not match, end loop

test_case_one = ["flower", "flow", "flight"]
print("test 1", longestCommonPrefix(test_case_one))

test_case_two = ["dog","racecar","car"]
print("test 2", longestCommonPrefix(test_case_two))
