# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = None
        head1 = None
        if l1 != None and l2 != None:
            
            if l1.val > l2.val:
                head1 = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                head1 = l1
                l1 = l1.next
            list1 = head1
            #print(list1)
        
            while l1 != None and l2 != None:
                if (l1.val > l2.val):
                    list1.next = l2
                    list1 = list1.next
                    l2 = l2.next

                else:# (l1.val <= l2.val):
                    list1.next = l1
                    list1 = list1.next
                    l1 = l1.next
                #print(list1.val)    
            if l1 != None:
                list1.next = l1
            elif l2 != None:
                list1.next = l2
        elif l1 != None:
            head1 = l1
        elif l2 != None:
            head1 = l2
            
        return head1
                
        