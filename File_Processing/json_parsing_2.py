# Coursera Python Specialization Example
# Source_input in dictionary format

import json
source_input = '''{
        "name":"Chuck",
        "phone":{
            "type":"intl",
            "number":"+1 734 303 4456"
                },
        "email":{
            "hide":"yes"
                }
        }'''

info = json.loads(source_input)
print('Name : ', info['name'])
print('Hide : ', info['email']['hide'])

