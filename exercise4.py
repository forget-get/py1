import re
# a = re.findall(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com$','13220032466@qq.com')
# print(a)


# b = re.findall(r'yaotao',a)
# print(b)

# b = re.findall(r'姚涛....',a)
# print(b)

# b = re.findall(r'.',a)
# print(b)
#
# b = re.findall(r'^.',a) # ^ 行首
# print(b)

# b = re.findall(r'yaotao$',a) # $ 行尾
# print(b)


# a = 'yaotaonihaow我是姚涛0508姚涛871YAOTAOoshiyaotao'
# b = re.findall(r'yaotao',a)  #\b \b 单词边界（一个独立的单词）
# print(b)


# a = 'yaotaonihaow我是姚涛0508姚涛871YAOTAOoshiyaotao'
# b = re.findall(r'(yaotao){1}',a)  #\b \b 单词边界（一个独立的单词）
# print(b)


a = 'asssssd'
b = re.findall(r'as{1}d',a)   # { } 控制次数
print(b)








