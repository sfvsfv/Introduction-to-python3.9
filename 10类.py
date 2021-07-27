"""
作者：川川
时间：2021/7/27
"""
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.r,x.i)
'''实例对象¶'''
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter
'''9.3.4. 方法对象'''
''''通常，方法在绑定后立即被调用'''
# class MyClass:
#     """A simple example class"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
# x=MyClass()
# xf = x.f
# while True:
#     print(xf())


'''9.3.5. 类和实例变量'''
# class Dog:
#     kind = 'canine'
#     def __init__(self, name):
#         self.name = name
# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.name)
# print(e.name)
# print(d.kind)

''''正确的类设计应该使用实例变量:'''
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# e.add_trick('play dead')
# # print(d.tricks)
# print(e.tricks)


''''迭代器'''
# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)
# for line in open("workfile"):
#     print(line, end='')


'''生成器'''
# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
#
# for char in reverse('golf'):
#     print(char)

'''生成器表达式'''
# a=sum(i*i for i in range(10))
# print(a)
# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# c=sum(x*y for x,y in zip(xvec, yvec))
# print(c)
