# XML Parsing | Coursera - Python Specialization Course | Example - 1

import xml.etree.ElementTree as ET
data = '''<person>
            <name>Chuck</name>
            <phone>+1 734 303 4456</phone>
            <email hide="yes"/>
        </person>'''
# Email element has the attribute of hide = 'yes' and it doesn't seem to store any data
# as there exists the self closing tag without any data

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
