"""
作者：川川
时间：2021/7/27
"""
'''在字符串开头的引号/三引号前添加 f 或 F 。在这种字符串中，可以在 { 和 } 字符之间输入引用的变量'''
# year = 2021
# event = 'Referendum'
# a=f'Results of the {year} {event}'
# print(a)
'''str.format() 该方法也用 { 和 } 标记替换变量的位置a  这种方法支持详细的格式化指令'''
# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
# a='{:-5} YES votes  {:1.1%}'.format(yes_votes, percentage)#调整{}内部感受下
# print(a)


'''只想快速显示变量进行调试，可以用 repr() 或 str() 函数把值转化为字符串。'''
# s = 'Hello, world.'
# print(str(s))#str() 函数返回供人阅读的值
# print(repr(s))#repr() 则生成适于解释器读取的值
# print(str(1/7))
# hellos = repr('hello')
# print(hellos)

'''7.1.1. 格式化字符串字面值'''
'''格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 f 或 F，通过 {expression} 表达式，把 Python 表达式的值添加到字符串内'''
'''下例将 pi 舍入到小数点后三位'''
# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')
'''在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐'''
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')


'''7.1.2. 字符串 format() 方法'''
# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
'''花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。花括号中的数字表示传递给 str.format() 方法的对象所在的位置。'''
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))
'''使用关键字参数名引用值。'''
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
'''位置参数和关键字参数可以任意组合'''
# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
#                                                        other='Georg'))

'''用方括号 '[]' 访问键来完成'''
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
'''也可以用 '**' 符号，把 table 当作传递的关键字参数。'''
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

'''生成一组整齐的列，包含给定整数及其平方与立方'''
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))


'''7.1.3. 手动格式化字符串'''
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     print(repr(x * x * x).rjust(4))

'''7.1.4. 旧式字符串格式化方法'''
# import math
# print('The value of pi is approximately %5.3f.' % math.pi)


'''7.2. 读写文件¶'''
'''最常用的参数有两个: open(filename, mode)'''
# f = open('workfile', 'w')
'''
第一个实参是文件名字符串第二个实参是包含描述文件使用方式字符的字符串。
mode 的值包括 'r' ，表示文件只能读取；'w' 表示只能写入（现有同名文件会被覆盖）；
'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。'r+' 表示打开文件进行读写。
mode 实参是可选的，省略时的默认值为 'r'。
'''
# with open('workfile') as f:
#     read_data = f.read()
#     print(read_data)
# f.close()#如果没有使用 with 关键字，则应调用 f.close() 关闭文件，即可释放文件占用的系统资源。

# with open('workfile') as f:
#     a=f.read()
#     print(a)
# f.close()

'''f.readline() 从文件中读取单行数据'''
# with open('workfile') as f:
   # a=f.readline()
   # b=f.readline()
   # c=f.readline()
   # print(a,b,c)
   # for i in f:
   #     print(i)
# f.close()

'''从文件中读取多行时，可以用循环遍历整个文件对象'''
# with open('workfile') as f:
#     for line in f:
#         print(line, end='')
# f.close()

'''f.write(string) 把 string 的内容写入文件，并返回写入的字符数。'''
# with open('workfile','w') as f:
#     f.write('This is a test\n')
# f.close()

'''写入其他类型的对象前，要先把它们转化为字符串（文本模式）或字节对象（二进制模式）'''
# with open('workfile','a') as f:
#     value = ('the answer', 42)
#     s = str(value)
#     f.write(s)
# f.close()

# f = open('workfile', 'rb+')
# f.write(b'0123456789abcdef')
# print(f.read())
# print(f.seek(5))
# print(f.read(1))

'''7.2.2. 使用 json 保存结构化数据'''
# import json
# a=json.dumps([1, 'simple', 'list'])
# print(a)
'''dumps() 函数还有一个变体， dump() ，它只将对象序列化为 text file '''
#如果 f 是 text file 对象
# json.dump(x, f)
#要再次解码对象，如果 f 是已打开、供读取的 text file 对象
# x = json.load(f)
