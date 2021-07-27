"""
作者：川川
时间：2021/7/27
"""

'''if语句固定搭配'''
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')
'''if ... elif ... elif ... 序列看作是其他语言中 switch 或 case 语句的替代品。'''


'''for语句'''
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     # print(w, len(w))


''' range() 函数用于遍历数字序列'''
# for i in range(5):
#     print(i)

'''range包左不包右'''
# for i in range(5, 10):
#     print(i)

'''range 可以不从 0 开始，还可以按指定幅度range(起点，终点，步长)'''
# for i in range(0, 10, 3):
#     print(i)
# for j in range(-10, -100, -30):
#     print(j)

'''range() 和 len() 组合在一起，可以按索引迭代序列'''
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

'''使用sum和range求连加和'''
# print(sum(range(5)))    #0 + 1 + 2 + 3+4

'''range 生成列表解决'''
# print(list(range(4)))


'''质数判断'''
#仔细看：else 子句属于 for 循环，不属于 if 语句。
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n // x)
#             break
#     else:
#         print(n, 'is a prime number')


'''continue 语句也借鉴自 C 语言，表示继续执行循环的下一次迭代：'''
# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)


#pass
'''pass 语句不执行任何操作'''
# while True:
#     pass
'''下面这段代码创建了一个最小的类'''
# class MyEmptyClass:
#     pass
'''pass 还可以用作函数或条件子句的占位符'''
# def initlog(*args):
#     pass
