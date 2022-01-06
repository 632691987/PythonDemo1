def helo1():
    print("Hello world")

helo1()


def hello(name):
    print("hello world:", name)

hello("vincent")


def hello3(name="koma"):
    print("hello world:", name)

hello3()
hello3("vincent")

def add(x, y):
    return x+y;

print(add(10,20))



def add(*nums):#看成是数组
    result = 0
    for val in nums:
        result = result + val
    print(result)

add(1,2,3,4,5)


def add23(**nums):#看成是字典
    for key in nums.keys():
        print(nums[key])

add23(
    key1=124,
    key2="value123"
)