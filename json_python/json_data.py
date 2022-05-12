import json

data = ['foo', {'bar': ('baz', None, 1.0, 2)}]

py_str = str(data)

json_str = json.dumps(data)

py_data_2 = json.loads(json_str)

print(json_str)

print(py_str)

print(py_data_2)

# print(json.dumps("\"foo\bar"))

# print(json.dumps('\u1234'))

# print(json.dumps('\\'))

# print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

# from io import StringIO
# io = StringIO()
# json.dump(['streaming API'], io)
# io.getvalue()
