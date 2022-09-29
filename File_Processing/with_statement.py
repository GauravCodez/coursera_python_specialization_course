# Using the with command to open and perform operations on the text file

with open("text_file.text") as myFiles:
    content = myFiles.read()

print(content)

# No need to close the file with the with statement as, with statement closes the
# file implicitly

