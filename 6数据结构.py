"""
作者：川川
时间：2021/7/27
"""

"""5.1 列表详解"""
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
'''
list.count(x)
返回列表中元素 x 出现的次数
'''
# print(fruits.count('apple'))
'''
list.index(x[, start[, end]])
返回列表中第一个值为 x 的元素的零基索引位置，第一个！
'''
# print(fruits.index('banana'))
# print(fruits.index('banana', 4,7))
'''
list.reverse()
反转列表中的元素。
'''
# fruits.reverse()
# print(fruits)
'''
list.append(x)
在列表末尾添加一个元素
'''
# fruits.append('grape')
# print(fruits)
'''
list.sort(*, key=None, reverse=False)
就地排序列表中的元素
'''
# fruits.sort()
# print(fruits)
'''
list.pop([i])
删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，a.pop() 删除并返回列表的最后一个元素。
'''
# fruits.pop()#默认删除最后一个
# print(fruits)
# fruits.pop(0)#删除第一个
# print(fruits)
'''
list.copy()
返回列表的浅拷贝,复制
'''
# fruits.copy()
# print(fruits)
'''
list.clear()
删除列表里的所有元素，相当于 del a[:] 。
'''
# fruits.clear()
# print(fruits)
'''
list.remove(x)
从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常。
'''
# fruits.remove('apple')
# print(fruits)
'''
list.insert(i, x)
在指定位置插入元素。第一个参数是插入元素的索引，因此，a.insert(0, x) 在列表开头插入元素
'''
# fruits.insert(1, 'nana')
# print(fruits)




'''用列表实现堆栈'''
'''
特点：“后进先出” 把元素添加到堆栈的顶端，使用 append() 。从堆栈顶部取出元素，使用 pop() ，不用指定索引。
'''
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

'''用列表实现队列'''
'''特点：“先进先出” 实现队列最好用 collections.deque，可以快速从两端添加或删除元素'''
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print(queue)
# print(queue.popleft())#第一个
# print(queue.popleft())#第二个
# print(queue)


''''列表推导式'''
'''创建平方值的列表'''
# squares = []
# for x in range(10):
#     squares.append(x ** 2)
# print(squares)
# b=squares = [x**2 for x in range(10)]
# print(b)
# a=squares = list(map(lambda x: x**2, range(10)))
# print(a)#同上

'''列表推导式将两个列表中不相等的元素组合起来'''
# a=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(a)
'''等价如下'''
# combs = []
# for x in [1,2,3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)


'''some example'''
# vec = [-4, -2, 0, 2, 4]
# print([x*2 for x in vec])
# print([x for x in vec if x >= 0])
# print([abs(x) for x in vec])#abs求绝对值

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# a=[weapon.strip() for weapon in freshfruit]
# print(a)
'''!!!!表达式是元组（例如上例的 (x, y)）时，必须加上括号'''
# b=[(x, x**2) for x in range(6)]
# print(b)

'''列表推导式可以使用复杂的表达式和嵌套函数'''
# from math import pi
# a=[str(round(pi, i)) for i in range(1, 6)]
# print(a)


'''嵌套的列表推导式'''
# matrix = [
# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
#     ]
# a=[[row[i] for row in matrix] for i in range(4)]
# print(a)
#等价如下
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)


'''5.2del 语句 移除元素'''
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[1]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)
'''del 也可以用来删除整个变量'''
# del a[:]
# print(a)


'''5.3元组和序列'''
'''元组由多个用逗号隔开的值组成'''
# t = 12345, 54321, 'hello!'#输入时，圆括号可有可无，不过经常是必须的
# print(t[0])
# print(t)    #输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组

# empty = ()
# singleton = 'hello',    #注意不加逗号就成了字符串了
# print(len(empty))
# print(len(singleton))
# print(singleton)


'''5.4集合'''
'''创建空集合只能用 set()，不能用 {}，{} 创建的是空字典'''
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)

# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a-b)
# print(a|b)#并集  letters in a or b or both
# print(a & b)#交集  etters in both a and b
# print( a ^ b)# # letters in a or b but not both

'''集合也支持推导式'''
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

'''5.5字典'''
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127 #添加
# print(tel)
# print(tel['jack'])#索取
# del tel['sape']
# tel['irv'] = 4127
# print(tel)
# print(list(tel))#转换为列表
# print('guido' in tel)
'''dict() 构造函数可以直接用键值对序列创建字典'''
# a=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(a)
# print(a['sape'])
'''字典推导式可以用任意键值表达式创建字典'''
# a={x: x**2 for x in (2, 4, 6)}#lamda
# print(a)
'''关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷'''
# c=dict(sape=4139, guido=4127, jack=4098)
# print(c)
# print(c['jack'])



'''5.6循环的技巧'''
'''在字典中循环时，用 items() 方法可同时取出键和对应的值'''
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k,v)
'''在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值'''
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i,v)
'''同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配'''
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))#0和1只是占位，不起作用，可以空着
'''逆向循环序列时，先正向定位序列，然后调用 reversed() 函数'''
# for i in reversed(range(1, 10, 2)):
#     print(i)
'''按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新的序列'''
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)
'''使用 set() 去除序列中的重复元素。使用 sorted() 加 set() 则按排序后的顺序，循环遍历序列中的唯一元素'''
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)
'''一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全'''
# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)#筛选出数字


'''5.7. 深入条件控制¶'''
'''布尔运算符 and 和 or 也称为 短路 运算符：其参数从左至右解析，一旦可以确定结果，解析就会停止。'''
# string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)#返回一个值
