def lengthOfLastWord(s):

    """This works, but did not achieve my goal of stripping all whitespace and is not very efficient"""

    # remove whitespace and tokenize string, originally used strip and split(" ") incorrectly

    wordList = s.split()
    print(wordList)

    # find last item in string, position [-1]
    # lastWord = wordList[-1]

    # return length of the last word, didnt need separate variable
    return len(wordList[-1])
  






test_case_1 = "Hello World"
print("test 1 ", lengthOfLastWord(test_case_1))

test_case_2 = "   fly me   to   the moon  "
print("test 2 ", lengthOfLastWord(test_case_2))

test_case_3 = "luffy is still joyboy"
print("test 3 ", lengthOfLastWord(test_case_3))
