

 #  在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
 #  请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 #
 #  解决方案一:
 #      采用递归的方式,一个是横坐标+1,一个是纵坐标+1,如果二者中存在一个为真,则是返回真,否则返回false
 #      注意点:在这个过程中需要记录数组的长度,保证值不超过数据下标
 #
 #  解决方案二:
 #      采用遍历的方式,遍历每一个数据
 #
 #  解决方案三:
 #      从左下角来看向上的都是自增

class Solution:
    # array 二维列表
    def Find(self, target, array):

        rows = len(array)
        cols = len(array[0])
        i=rows -1
        j=0
        while i>=0 and j<=cols-1:
            if target<array[i][j]:
                i =i-1
            elif target>array[i][j]:
                j = j+1
            else:
                return True
        return False