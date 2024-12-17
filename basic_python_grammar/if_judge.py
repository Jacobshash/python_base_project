a = 123
b = 1.23
c = "123"
d = '123'
e = 4 + 5j
f = True
g = None
h = b'123'
# 不可变
i = (a, b, c, d, e, f, g, h)
# 可变
j = [a, b, c, d, e, f, g, h]
k = {'name': 'lol', 'age': 18}
l = {'name', 'lol', 'age', 18}
# 不可变
o = frozenset({'name', 'lol', 'age', 18})


def if_method(names):
    for name in names:
        if type(name) == int:
            print(f"{name} \t ==> is int")
        elif type(name) == float:
            print(f"{name} \t ==> is float")
        elif type(name) == str:
            print(f"{name} \t ==> is str")
        elif type(name) == complex:
            print(f"{name} \t ==> is complex")
        elif type(name) == bool:
            print(f"{name} \t ==> is bool")
        elif type(name) == type(None):
            print(f"{name} \t ==> is None")
        elif type(name) == bytes:
            print(f"{name} \t ==> is bytes")
        elif type(name) == tuple:
            print(f"{name} \t ==> is tuple")
        elif type(name) == list:
            print(f"{name} \t ==> is list")
        elif type(name) == dict:
            print(f"{name} \t ==> is dict")
        elif type(name) == set:
            print(f"{name} \t ==> is set")
        else:
            print(f"{name} \t ==> is {type(name).__name__}")


array = [a, b, c, d, e, f, g, h, i, j, k, l, o]
if_method(array)

a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

a = [1, 2, 3, 4]
b = a
print(id(a))
print(id(b))
if (a is b) and (a == b) and (id(a) == id(b)):
    print("1 - a 和 b 有相同的标识，并且 a 等于 b")
else:
    print("1 - a 和 b 没有相同的标识，或者 a 等于 b")

a = [1, 2, 3, 4]
b = a[:]
print(id(a))
print(id(b))
if (a is b) and (a == b):
    print("1 - a 和 b 有相同的标识，并且 a 等于 b")
else:
    print("1 - a 和 b 没有相同的标识，或者 a 等于 b")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")
