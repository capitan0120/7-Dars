class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        llist = []
        while head:
            llist.append(head.val)
            head = head.next

        curr = ListNode(0)
        temp = curr
        for i in llist[::-1]:
            temp.next = ListNode(i)
            temp = temp.next
        return curr.next