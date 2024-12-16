a = 123
b = 1.23
c = "123"
d = '123'
e = 4+5j
f = True
g = None
h = b'123'
# 不可变
i = (a, b,c,d,e,f,g,h)
# 可变
j = [a,b,c,d,e,f,g,h]
k = {'name':'lol','age':18}
l = {'name','lol','age',18}
# 不可变
o = frozenset({'name','lol','age',18})

def if_method(names):
    for name in names:
        if type(name) == int:
            print(f"{name} is int")
        elif type(name) == float:
            print(f"{name} is float")
        elif type(name) == str:
            print(f"{name} is str")
        elif type(name) == complex:
            print(f"{name} is complex")
        elif type(name) == bool:
            print(f"{name} is bool")
        elif type(name) == type(None):
            print(f"{name} is None")
        else :
            print(f"{name} is unknown")
