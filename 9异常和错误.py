"""
作者：川川
时间：2021/7/27
"""
'''处理异常搭配：try except'''
'''如果没有异常发生，则跳过 except 子句 并完成 try 语句的执行。'''
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

'''一个 try 语句可能有多个 except 子句，以指定不同异常的处理程序。'''
# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

'''最后的 except 子句可以省略异常名，以用作通配符'''
# try:
#     f = open('workfile')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


'''try ... except 语句有一个可选的 else 子句，在使用时必须放在所有的 except 子句后面'''
# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()


'''处理 try 子句中调用（即使是间接地）的函数内部发生的异常。'''
# def this_fails():
#     x = 1 / 0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

'''raise 语句支持强制触发指定的异常'''
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


'''异常链'''
# def func():
#     raise IOError
# try:
#     func()
# except IOError as exc:
#     raise RuntimeError('Failed to open database') from exc



'''异常链在 except 或 finally 子句触发异常时自动生成'''
# try:
#     open('database.sqlite')
# except IOError:
#     raise RuntimeError from None

'''定义清理操作'''
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

'''一个更为复杂的例子'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
print(divide(2,1))
