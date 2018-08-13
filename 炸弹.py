# coding=utf-8
from multiprocessing import Process
import os
import time
G_boom_num = 1

def boom():
    print("炸弹的进程号为%d"%os.getpid())
    pass
# 主函数
def main():
    global G_boom_num
    while True:
        # 创建一个炸弹(子进程)
        bo = Process(target = boom)
        # 引爆炸弹...
        bo.start()
        # 为炸弹计数
        G_boom_num += 1
        print("创建第%d个炸弹"%G_boom_num)
        # 创建一个炸弹后延时2秒钟,如果想试试进程炸弹的威力,可以把下面这行注释掉...
        # time.sleep(2)

# 开启入口,启动主程序
if __name__ == "__main__":
    main()



