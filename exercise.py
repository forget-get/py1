#  #第一天
# import  decimal
# a = decimal.Decimal('9.4')
# b = decimal.Decimal('8.9')
# import math
# print(math.floor(4.5))
# print(math.ceil(5.2))
# print(6)
# a = 1,2,3,4
# print(a)
# print(type(a))
# a = 'HelloWorld'
# print(a)
# li = [3.4,6,6,66,6666,6]
# print(type(li))
# tu = (3,2,4)
# print(tu)
# print(type(tu))
# print(li[-2])
# print(li[2::1])
# print(6 in li)
# li = [1,2,3]
# a,s,d = li
# print(a,s,d)
# li = ['123','456','789']
# a,*b = li
# print(b)
# # 第二天
# li = [2,3.4,'567',True]
# li.append('你好，世界')   #添加
# print(li)
# li.extend('aaa')   #添加的字符被切割
# print(li)
# li.extend('123')
# print(li)
# li.insert(3,False)   #索引添加
# print(li)
# li.pop(-1)   #索引删除
# print(li)
# li.remove('1')  #指定删除
# print(li)
# li.clear()#全部删除
# print(li)
# li[-1] = 'd'#索引修改
# print(li)
# print(li.index('你好，世界'))#查看索引值
# print(li.count('a'))#查看元素出现的次数
# a = li.copy()#浅复制
# print(a)
# li = [1,3,4,5,2,3,6,7,1]
# li.sort()#正向排序
# print(li)
# li.sort(reverse=True)#直接反向排序
# print(li)
#
#
# tu = (1,1,1,21,3,4)
# print(tu.count(1))#查看元素出现的次数
# print(tu.index(3))#查看元素索引值
# li = [2,3.4,'567',True]
# a = str(li)#转换
# print(type(a))
# print(a)
# print(id(a))#查看内存地值
#
#
# a = 'asd fea 1235 asd'
# #查
# print(a.count('a'))#查看元素出现的次数
# print(a.index('e'))#查看元素索引值(没有会报错)
# print(a.find('q'))#查看元素的索引值（没有不会报错 ，会返回 -1）
# print(a.isdigit())#判断字符串中的内容是否是全是数字
# print(a.isalpha())#判断字符串中的内容是否全是字母
# print(a.endswith('ea'))#判读字符以什么结尾
# print(a.startswith('as'))#判断字符串以什么开始
# print(a.islower())#判断字符串的字母是不是全是小写
# print(a.isupper())#判断字符串的字母是不是全是大写
#
# # 改（不修改原来的字符串）
# print(a.lower())#把字母全部变成小写的
# print(a.upper())#把字母全变成大写的
# print(a.strip())#移除前后空格  lstrip(只移除左边的空格)  rstrip(只移除右边的空格)
# print(a.capitalize())#如果字符串第一个是字母就把这一个字母变成大写的
# print(a.title())#将英语句子每个单词的首字母大写
# print(a.split('as',1))#切割
#
# #删
# print(a.replace('asd','qwe',1))#替换
#
#
# a = 'asdf\nasdf'# \n 换行
# print(a)
# a = 'asd\tasdf'# \t 四个空格
# print(a)
# a = 'asdf\bas'# \b  退格(删除)
# print(a)
# a = 'asdf\r22'# \r  删除前面的内容
# print(a)
# a = 'asdf\'dea'# \\ 代表一个反斜杠   \' 代表一个单引号
# print(a)
# a = r'asdf\ssadf\tasdf\nasdf'#防止字符串被转义
# print(a)
#
# a = '我的未来'.encode('UTF-8')# 加密
# print(a)
#
# a =b'\xe6\x88\x91\xe7\x9a\x84\xe6\x9c\xaa\xe6\x9d\xa5' .decode('UTF-8')#解密
# print(a)
#
#
#
# a = '123'
# b = '456'
# c = '789'
# print(a + b + c )#字符串拼接  直接相加
#
# print('%.4f'%11.22548913) # (% .?) 四舍五入后小数点后几位
# print('%s是%s'%('姚涛','菜鸟'))# %s 占位符
# a = '132464'
# print(','.join(a))#  '要加的内容'.join（）
# print('{}{}{}'.format('woshi','yaotao','shicainiao'))# 使用{}.format拼接
# print('你好{2}，我是{0}，你要{1}'.format('菜鸟','努力了','姚涛'))#使用{索引值}.format拼接
# print('{a}{b}{c}'.format(a = 1,b = 2,c = 3))#指定值赋值添加
# a = '我是,{}'.format
# print(a('姚涛'))
#
# se = {'a','a','v','e'}
# print(se)
# print(se.add('u'))  #增加一个值
# print(se)
# print(se.pop())#随机删除一个值
# print(se)
# print(se.remove('e'))#指定删除一个值
# print(se)
# se.update('156')#指定添加值(什么都可以添加)
# print(se)
#
#
# di = ({'age':18})
# print(di)
# di['name'] = 'yaotao'#增加一个键值对
# print(di)
# print(di.get('sex'))#用键去查值
# di['sex'] = '男' #输入键再原字典有就 改， 无就 增
# print(di)
# # a = di.fromkeys(di) #取出 di 字典中全部的键赋值给a
# # print(a)
# a = di.fromkeys(di,666) # 取出字典所有的 键 并把 666 赋值个 值
# print(a)
# print(di.setdefault('爱好','耍'))  #有键就查值，无键就增键值对
# print(di)
# print(di.pop('爱好'))  #输入键指定删除键值对
# print(di)
# print(di.popitem())  #随机删除一个键值对
# print(di)
# print(di.update({'name':'yaotao'})) #新增一个键值对
# print(di)
# di.update(aihao = 'shua')  #新增一个键值对
# print(di)
# b = di.keys()  #取出字典所有的键
# print(b)
# c = di.values()  #取出字典所有的值
# print(c)


# li = [1,  5,  6,  9,  3,  2]
# i  =  0
# while   i < len(li):
#       print(True) if li[i] > 5 else  False
#       i += 1
# li = [1,  5,  6,  9,  3,  2]
# for i in li:
#     print(i,end=' ')

# for a in range(1,10):
#     for b in range(1,10):
#         if a >= b :
#             print('%s X %s = %s'%(b,a,a*b),end='  ' )
#     print()
# for i in range(100):
#     if i % 11 == 0:
#         print(i,end=" ")
# print('Who do you think I am?')
# you = input()
# print('你说折谁就是谁:')
# print(you)
print('He said,"I\'m yours!"')