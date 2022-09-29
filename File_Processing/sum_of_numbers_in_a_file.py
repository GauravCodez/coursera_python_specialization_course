# From the text file get the sum of all the numbers using regular expressions
import re

file = open('regex_sum_1653652.txt')
listted = list()
total = 0
for line in file:
    line = line.rstrip()
    number_string = re.findall("[0-9]+", line)

    for word in number_string:
        listted.append(int(word))

print(sum(listted))
