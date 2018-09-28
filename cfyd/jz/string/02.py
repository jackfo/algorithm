#
#解决方案一:
#    构造一个新的字符串,将原字符串追加进去,如果碰到空格,则追加内容为%20
#解决方案二:
#    先计数新的空格的个数,并构造新的字符字符串数组大小
#    从最后一个字符串开始进行操作
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s=list(s)
        count = len(s)

        for i in range(0,count):
            if s[i] =='':
                s[i]='%20'
                return ''.join(s)