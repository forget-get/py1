# def func(num):
#     a = 0
#     b = 1
#     n = 0
#     while n<num:
#         a,b = b,a+b
#         n += 1
#         yield a
# c = func(30)
# for i in c:
#     print(i,end=' ')




# for i in range(1,10):
#     for b in range(1,10):
#         if i >= b:
#             print('%s X %s = %s'%(b,i,i*b),end=" ")
#     print()




# tu = (1,2,3,4)
# a, *b, c = tu
# print(a)
# print(b)
# print(c)



# li = [i for i in range(100)]   #生成一个列表
# print(li)
#
# x = (i for i in range(100))   #小括号就是一个生成器
# print(type(x))


# di = {'姓名':'yaotao','年龄':18}
# print(di.setdefault('年龄'))
# print(di.setdefault('性别','男'))
# print(di)
#



# for i in range(10):
#     for j in range(i + 1):
#         print('*',end=' ')
#     print()

# for i in range(1,50,2):   #range(起，终，步长)
#     print(i,end=' ')



# def a(q):
#     if q == 1 :
#         print('你好')
# a(int(input('请输入：')))


# import this


def fib(num):
    a = 0
    b = 1
    n = 0
    while n < num:
        a, b = b , a+b
        n += 1
        yield a

c = fib(int(input('请输入要计算的个数：')))
for i in c:
    print(i,end=' ')













