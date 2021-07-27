"""
作者：川川
时间：2021/7/27
"""
'''单引号和双引号效果相同  反斜杠 \ 用于转义'''
# a='spam eggs'
# b='doesn\'t'
# c="\"Yes,\" they said."
# print(a)
# print(b)
# print(c)


'''如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r '''
#比如说我们路径问题
# c=r'C:\some\name'
# print(c)
# print(r'C:\some\name')


'''三引号使用'''
# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)


'''字符串可以用 + 合并（粘到一起），也可以用 * 重复'''
# a='how are '+'you'
# b='zhu'
# c=b*3
# print(a)
# print(c)


'''相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并'''
# a= 'Py'     'thon'
# print(a)


'''拆分长字符串'''
# text = ('Put several strings within parentheses '
#         'to have them joined together.')
# print(text)


    ######### 切片#########
'''字符串支持 索引 （下标访问），第一个字符的索引是 0。'''
# word = 'Python'
# print(word[0],word[2])
'''索引还支持负数，用负数索引时，从右边开始计数'''
# print(word[-1],word[-2])
# text='s'
# print(text[0])
'''除了索引，字符串还支持 切片。输出结果包含切片开始，但不包含切片结束'''
# print(word[0:2])
# print(word[0:5])
'''省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾'''
# print(word[:2])
# print(word[4:])
# print(word[-2:])
'''切片会自动处理越界索引'''
# print(word[4:42])
# print(word[42:])
''' 字符串不能修改'''
# word[0] = 'J'#错误
'''要生成不同的字符串，应新建一个字符串'''
# z='J' + word[1:]
# print(z)


'''内置函数 len() 返回字符串的长度,一个空格也算一个长度'''
# s = 'supercalifragilisticexpia lidocious'
# print(len(s))
