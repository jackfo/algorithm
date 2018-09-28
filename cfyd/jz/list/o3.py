# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方案一: 采用递归的方式

# 方案二: 集合之间采用相加的方式
#        从最后一个加到第一个
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]