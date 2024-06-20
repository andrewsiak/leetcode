
def mergeTwoLists(list1, list2):
    # create a new empty list
    # if list1 and list 2 are empty return new_list 
    # if list1[0] exists
    # check if less than or equal to list 2 index 0
    # if true, pop and add to new_list
    # if false, pop list2[0] and add to new list

    new_list = []
    if list1 == [] and list2 == []:
        return new_list
    if list1 == [] and list2 != []:
        return list2
    while list1 and list2:
        if list1[0] <= list2[0]:
            new_list.append(list1[0])
            list1.pop(0)
        else:
            new_list.append(list2[0])
            list2.pop(0)
        
            

test1_list1 = [1,3,5]
test1_list2 = [2,4,6]
print("Case 1", mergeTwoLists(test1_list1, test1_list2))

test2_list1 = [1,1]
test2_list2 = [0,2]
print("Case 2", mergeTwoLists(test2_list1, test2_list2))

test3_list1 = []
test3_list2 = [1]
print("Case 3", mergeTwoLists(test3_list1, test3_list2))
