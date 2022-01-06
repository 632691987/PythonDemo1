# 切片是按照值去复制的，而如果 def1 = abc 则是按照地址复制的

abc = ["aa","bb", "cc"]

def1 = abc[1:]

def1[0] = "dd"

print(abc)
print(def1)