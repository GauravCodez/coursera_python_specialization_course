# JSON parsing where source input is in List format

import json
source_input = '''[{"id":"001",
            "x":"2",
            "name":"Charles"},
            {"id":"009",
            "x":"4",
            "name":"Chuck"}
            ]'''
info = json.loads(source_input)
print("user count : ", len(info))
for item in info:
    print("Name : ", item['name'])
    print("Id : ", item['id'])
    print("Attribute : ", item['x'])
