def a(q):
    if q == '乘法表'or q == 'cfb':
        for i in range(1,10):
            for j in range(1,10):
                if i>=j:
                    print('%s X %s = %s'%(j,i,i*j),end='  ')
            print()
    else:
        pass


def s(w):
    if w == '斐波那契数列' or w == 'fib':
        def fib(num):
            a = 0
            b = 1
            n = 0
            while n < num:
                a, b = b, a + b
                n += 1
                yield a

        c = fib(int(input('请输入要计算的个数：')))
        for i in c:
            print(i, end=' ')

    else:
        pass

a(input('请输入乘法表或者cfb(enter键下一个选项):'))
s(input('请输入斐波那契数列或者fib(enter键下一个选项)：'))

