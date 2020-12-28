import json
from collections import OrderedDict

jsondata = """{
    "name": "Leonie",
    "id":123,
    "a": {"bb": "ddd", "cc": "ddd"},
    "b": [
    {"ccc": "123", "123": 123},
    {"ddd": "456", "456": 456}
  ]
}"""
# 保持顺序一致
b = json.loads(jsondata, object_pairs_hook=OrderedDict)
# dumps方法 https://docs.python.org/3/library/json.html#json.dumps
c = json.dumps(b, sort_keys= False, indent=4, separators=(', ', ': '))
f2 = open('jsonBeispiel.json', 'w')
f2.write(c)
f2.close()