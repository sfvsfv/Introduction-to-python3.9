"""
作者：川川
时间：2021/7/27
"""

'''操作系统接口(个人感觉没啥用)'''
# import os
# print(os.getcwd())#打印出当前文件位置
# os.chdir('/server/accesslogs')#改变运行位置
# os.system('mkdir today') #运行这个再系统shell

'''文件通配符'''
'''glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数:'''
# import glob
# print(glob.glob('*.py'))

'''命令行参数'''
# import sys
# print(sys.argv)#打印本文件位置

''' 字符串模式匹配'''
# import re
# b=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# print(b)
# a='tea for too'.replace('too', 'two')
# print(a)

'''数学'''
# import math
# a=math.cos(math.pi / 4)
# print(a)

# import random
# b=random.choice(['apple', 'pear', 'banana'])
# print(b)

'''互联网访问'''
# from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#     for line in response:
#         line = line.decode('utf-8')  # Decoding the binary data to text.
#         if 'EST' in line or 'EDT' in line:
#             print(line)

# smtplib 用于发送邮件
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org')
# server.quit()


''' 日期和时间'''
# from datetime import date
# now = date.today()
# print(now)
# a=now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# print(a)
# birthday = date(2000, 9, 20)
# age = now - birthday
# c=age.days
# print(c)

'''数据压缩'''
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print( zlib.decompress(t))
# print(zlib.crc32(s))

'''性能测量'''
# from timeit import Timer
# a= Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# print(a)
