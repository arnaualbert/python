import json

data = ['foo', {'bar': ('baz', None, 1.0, 2)}]

py_str = str(data)

json_str = json.dumps(data) # convierte python a json

py_data_2 = json.loads(json_str) # convierte json a python

print(json_str)

print(py_str)

print(py_data_2)