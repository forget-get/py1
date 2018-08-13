# coding=utf-8
# import datetime
# import time
# date = datetime.date(2018,8,8)
# print(date)
# time = datetime.time(9,47)
# print(time)
# dt = datetime.datetime(2018,8,8,9,47)
# print(dt)
# delta = datetime.timedelta(hours=16)
# print(delta)
# print(dt + delta)
# now = datetime.datetime.now()
# print(now)
# utc = datetime.datetime.utcnow()
# print(utc)
# t2 = now.timestamp()
# print(t2)

# now = datetime.datetime.now()
# print(now.isoformat())

# def how_long(year,month,day,hour=0,minut=0,second=0):
#     now = datetime.datetime.now()
#     print(now)
#
#     btime = datetime.datetime(year,month,day,hour,minut,second)
#     print(btime)
#
#     time = now - btime
#     print('你活了:',time)
#
# how_long(2000,5,8)

import logging
#第一步，定义logger对象
logger = logging.getLogger('error.log') #日志取名
logger.setLevel(logging.DEBUG)  #设置日志级别

#第二部，定义handler
#1、建立filehondler来把日志记录在文件里，设置级别为debug以上
fh = logging.FileHandler('error.log')  #写入文件
fh.setLevel(logging.DEBUG)  #写入文件的级别
#2、建立streamhandler来把日志，打印到控制台，设置级别为error以上
ch = logging.StreamHandler()    #控制台输出
ch.setLevel(logging.ERROR)  #控制台输出的级别

#第三部，自定义日志格式
formatter = logging.Formatter("错误时间：%(asctime)s 日志名字：%(name)s 日志消息：%(message)s")    #日志格式
ch.setFormatter(formatter)  #控制台按照这种格式输出
fh.setFormatter(formatter)  #文件按照这种格式输出

#第四部，将相应的handler添加到logger对象中
logger.addHandler(ch)   #启动
logger.addHandler(fh)   #启动

#测试
if __name__ == '__main__':
    logger.debug('测试')
    logger.info('正常')
    logger.warn('警告')
    logger.error('出错')
    logger.critical('王炸')
    def fun(a):
        try:
            num = 20 / a
            logger.info(num)
        except Exception as e:
            logger.error(e)
    fun(0)