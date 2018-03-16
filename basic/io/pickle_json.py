# -*- coding: utf-8 -*-

import pickle
import json

# d = dict(name = 'Bob', age = 20, score = 88)
# print(pickle.dumps(d))

# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# print(d)

# s = dict(s=['a', 'b', 'c', 'd'], a=1, b='sss')
# d = json.dumps(s)
# print(d)

# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# d = json.loads(json_str)
# print(type(d))

# ensure_ascii == True: ascii, False: 中文
obj = dict(name='小明', age = 20)
s = json.dumps(obj, ensure_ascii=False)
print(s)