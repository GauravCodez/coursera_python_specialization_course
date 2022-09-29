import re
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
x = re.findall('^From .*@([^ ]*)', data)
y = re.findall('@([^ ]*)', data)
print("way 1", y)
print("way 2", x)


