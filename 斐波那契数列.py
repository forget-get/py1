# -*- coding: utf-8 -*-
# 斐波那契数列（Fibonacci sequence），指的是这样一个数列：1、1、2、3、5、8、13、21、34
# 要求一：输出第10个斐波那契数列
# 要求二：输出指定个数的斐波那契数列
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    list = []
    fib(n)
    for i in range(1, n + 1):
        list.append(fib(i))
    print(list)


if __name__ == "__main__":
    n = int(input("请输入需要计算的个数："))
    print
    fib(n)
    fib_seq(n)
