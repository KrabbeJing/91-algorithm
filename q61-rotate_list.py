# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        # cur指向尾巴
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        # 如果k能被n整除，那么旋转后和原始一样
        if (add := n - k % n) == n:
            return head
        # 海象符，上面两行代码等于下面三行
        # add = n - k % n
        # if add == n:
        #     return head
        # 连接首尾 cur是尾巴
        cur.next = head
        # 找到新的尾巴
        while add:
            cur = cur.next
            add -= 1
        ret = cur.next
        cur.next = None
        return ret