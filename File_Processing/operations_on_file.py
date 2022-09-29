# Providing the count of words occuring in a file
xfile = open('text_file.text')

# reading the file
file_data = xfile.read()
# Splitting the file data into list of words
words_in_the_file = file_data.split()

print("List of words in the file")
print(words_in_the_file)
counts = dict()

for words in words_in_the_file:
    counts[words] = counts.get(words, 0) + 1

print("count of each word in the file ::")
print(counts)
