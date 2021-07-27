"""
作者：川川
时间：2021/7/27
"""


# squares = [1, 4, 9, 16, 25]
# print(squares)

'''支持索引和切片'''
# print(squares[1])
# print(squares[-1])
# print(squares[-3:])

'''列表还支持合并操作'''
# c=squares + [36, 49, 64, 81, 100]
# print(c)



'''列表内容可修改'''
# cubes = [1, 8, 27, 65, 125]
# cubes[3] = 64
# print(cubes)
'''append() 方法 可以在列表结尾添加新元素'''
# cubes.append(216)
# cubes.append(7 ** 3)
# print(cubes)


'''切片赋值可以改变列表大小，甚至清空整个列表'''
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# letters[2:5] = []
# print(letters)
# letters[:] = []
# print(letters)


'''内置函数 len() 也支持列表'''
# letters = ['a', 'b', 'c', 'd']
# print(len(letters))

'''还可以嵌套列表（创建包含其他列表的列表）'''
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)
# print(x[0])#索取
# print(x[0][1])

#while
'''斐波纳契数列，使得每个数字是两个前述者的总和，选自0和1。'''
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a + b

'''print'''
# i = 256*256
# print('The value of i is', i)

'''end 可以取消输出后面的换行, 或用另一个字符串结尾'''
# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a + b
