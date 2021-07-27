"""
作者：川川
时间：2021/7/27
"""

'''def 定义函数  斐波那契数列函数'''
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
# fib(100)    #传参


#返回列表
# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a + b
#     return result
# f100 = fib2(100)
# print(f100)

'''默认值在 定义 作用域里的函数定义中求值'''
# i = 5
# def f(arg=i):
#     print(arg)
# i = 6
# f()#输出5而不是6


'''默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。'''
# def f(a, L=[]):
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(3))


'''不想在后续调用之间共享默认值时，应以如下方式编写函数'''
# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
# print(f(10))
# print(f(11))

"""关键字参数"""
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
# # parrot(5)
# '''该函数接受一个必选参数（voltage）和三个可选参数（state, action 和 type）'''
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


'''*name 必须在 **name 前面'''
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


'''some example'''
# def standard_arg(arg):
#     print(arg)
# def pos_only_arg(arg, /):
#     print(arg)
# def kwd_only_arg(*, arg):
#     print(arg)
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
#来看看区别
#第一个对调用方式没有任何限制，可以按位置也可以按关键字传递参数
# print(standard_arg(2))
# print(standard_arg(arg=2))
#第二个  函数定义中有 /，仅限使用位置形参
# print(pos_only_arg(1))
# print(pos_only_arg(arg=1))#就会报错
#第三个 函数定义通过 * 表明仅限关键字参数
# print(kwd_only_arg(3))#就会报错
# print(kwd_only_arg(arg=3))
#第四个kwd_only_arg(arg=3)
# print(combined_example(1, 2, 3))#报错
# print(combined_example(1, 2, kwd_only=3))
# print(combined_example(1, standard=2, kwd_only=3))
# print(combined_example(pos_only=1, standard=2, kwd_only=3))#报错

'''加上 / （仅限位置参数）后，就可以了。此时，函数定义把 name 当作位置参数，'name' 也可以作为关键字参数的键'''
# def foo(name, /, **kwds):
#     return 'name' in kwds
# print(foo(1, **{'name': 2}))#返回tuue
# def foo(name, **kwds):
#     return 'name' in kwds
# print(foo(name=5))#返回false,实际这name没用到，所以哟弄个上面那个方法


'''解包实参列表'''
# print(list(range(3, 6)))
# args = [3, 6]
# print(list(range(*args)))#用 * 操作符把实参从列表或元组解包出来
'''字典可以用 ** 操作符传递关键字参数'''
# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)


"""Lambda 表达式"""
'''lambda a, b: a+b 函数返回两个参数的和'''
# def make_incrementor(n):
#     return lambda x: x + n
# f = make_incrementor(42)
# print(f(0))
# print(f(1))

