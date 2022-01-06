fileName = "abc.txt"

with open(fileName, 'w', encoding='utf-8') as myfile:
    myfile.write("hello")


with open(fileName, 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    print(content)