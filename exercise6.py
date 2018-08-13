# coding=utf-8
#import json
#print(json.__all__)
#ceshi ={'name':'yaotao','age':18}
# a = json.dumps(ceshi)
# print(a)
# b = json.loads(a)
# print(b)
# with open('test.json','w+') as f:
#     json.dump(ceshi,f)    #序列化
# with open('test.json','r') as f:
#     r = json.load(f)    #反序列化
#     print(r)

import hashlib
salt = 'nihao'
password = '111111'.encode('utf8') + salt.encode('utf8')
a = hashlib.new('md5',password)
print(a.hexdigest())
id = '111111'.encode('utf8')
b = hashlib.md5(id).hexdigest()
print(b)
c = hashlib.sha512(id)
print(c.hexdigest())











