#coding:utf-8　
#直接插入排序

class Solution:
    def insert_sort(array):
        for i in range(len(array)):
            for j in range(i):
                if array[i] < array[j]:
                    array.insert(j,array.pop(i))
        return array