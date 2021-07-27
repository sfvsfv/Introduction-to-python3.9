"""
作者：川川
时间：2021/7/27
"""
'''用文本编辑器在当前目录下创建 fibo.py 文件，输入以下内容'''
#这部分单独创建文件！在这展示fibo内容只是便于好看
# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# def fib2(n):   # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
'''这项操作不直接把 fibo 函数定义的名称导入到当前符号表，只导入模块名 fibo 。要使用模块名访问函数'''
# import fibo
# print(fibo.fib(1000))
'''如果经常使用某个函数，可以把它赋值给局部变量'''
# a = fibo.fib
# print(a(400))

'''6.1. 模块详解'''
'''import 语句有一个变体，可以直接把模块里的名称导入到另一个模块的符号表'''
# from fibo import fib, fib2
# print(fib(500))
'''还有一种变体可以导入模块内定义的所有名称 不建议从模块或包内导入 *， 因为，这项操作经常让代码变得难以理解。'''
# from fibo import *
# print(fib(500))
'''模块名后使用 as 时，直接把 as 后的名称与导入模块绑定。意思就是改变名称使用，'''
# import fibo as fib
# print(fib.fib(500))
'''from 中也可以使用这种方式'''
# from fibo import fib as fibonacci
# print(fibonacci(500))

