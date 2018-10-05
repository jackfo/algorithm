#coding:utf-8　
class Solution:
    def shell_sort(array):
        gap = len(array)
        while gap > 1:
            gap = gap // 2
            for i in range(gap,len(array)):
                for j in range(i%gap,i,gap):
                    if array[i] < array[j]:
                        array[i],array[j] = array[j],array[i]
        return array

    print shell_sort([0,2,1,3])