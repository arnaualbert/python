import json

# Data
data: list = ['foo', {'bar': ('baz', None, 1.0, 2)}]

# 1.Convert python data to json string
py_str:   str = str(data)
json_str: str = json.dumps(data)

print(py_str)
print(json_str)

# 2.Convert json string to python data
py_data2: list = json.loads(json_str)
print(py_data2)
