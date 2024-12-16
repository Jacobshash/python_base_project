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

m = """
this is multiline comment 
"""

n = '''
this is multiline comment 
'''

def method_name(name):
    for element in name:
        print(f"{element} \t ==> type is  {type(element)}")



array = [a,b,c,d,e,f,g,h,i,j,k,l,o,m,n]
method_name(array)
