# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

EXAMPLES:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

SOLUTION:
    get two list and merge them in one list
    check if the list are empty
    sorte and return the list
"""


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sorted_list = []
        if list1 == None and list2 == None:
            return False

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                sorted_list.append(list1.val)
                list1 = list1.next
            else:
                sorted_list.append(list2.val)
                list2 = list2.next

        return (sorted(sorted_list))


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(Solution().mergeTwoLists(list1, list2))
