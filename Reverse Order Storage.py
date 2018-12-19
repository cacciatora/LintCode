class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order
    """
    def reverseStore(self, head):
        if head == None:
            return []
        p = head
        array = []
        while p != None:
            array.append(p.val)
            p = p.next
        array.reverse()
        return array