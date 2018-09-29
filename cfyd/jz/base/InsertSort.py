#coding:utf-8　
#直接插入排序
#时间复杂度 O(n的平方)
#空间复杂度 O(1)
class Solution:
    def insert_sort(array):
        for i in range(len(array)):
            for j in range(i):
                if array[i] < array[j]:
                    array.insert(j,array.pop(i))
        return array



    print insert_sort([1,0])
    print eval("1+1-1+2")