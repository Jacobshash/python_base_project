print("-------------------------------------------------------------------------------------")
print("隐式类型转换")
# int + int = int
# int + float = float
# float + float = float

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:", type(num_int))
print("num_flo 数据类型为:", type(num_flo))

print("num_new 值为:", num_new)
print("num_new 数据类型为:", type(num_new))

# int + str = 报错
# float + str = 报错
# str + str = str
# char + str = str


num_int = 123
num_str = "456"

print("num_int 数据类型为:", type(num_int))
print("num_str 数据类型为:", type(num_str))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(num_int+num_str)

# TypeError: unsupported operand type(s) for +: 'float' and 'str'
# print(num_flo+num_str)

# TypeError: ord() expected a character, but string of length 3 found
# print(ord(num_str)+num_int)

num_str2 = "456"
print(num_str + num_str2)

num_char = 'A'
print(num_char + num_str)

print(ord(num_char))
# ord(num_char) 转为字符的ASCII码 'A'的值是65
print(ord(num_char) + num_int)

print("-------------------------------------------------------------------------------------")
print("显式类型转换")

num_char = 'A'

num_str = "abc"
num_str_a = "a"

num_str_int = "123"
num_int = 123

num_float = 1.23
num_float_str = "1.23"

num_complex = 1.23j

# ValueError: invalid literal for int() with base 10: 'A'
# print(int(num_char_A))

# ValueError: invalid literal for int() with base 10: 'abc'
# print(int(num_str_abc))

int_num_int = int(num_str_int) + num_int
print(f"{int_num_int}  \t\t type is {type(int_num_int)}")

str_num_float = float(num_float_str) + num_float
print(f"{str_num_float} \t\t  type is {type(str_num_float)}")

str_num_complex = complex(num_float_str) + num_complex
print(f"{str_num_complex} \t\t  type is {type(str_num_complex)}")

s = str(num_int)
print(f"{s} \t\t type is {type(s)}")
print(f"{num_int} \t\t  type is {type(num_int)}")

s = "12345678"
str_to_tuples = tuple(s)
str_to_list = list(s)
str_to_set = set(s)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
# str_to_dict = dict(s)
print(f"{str_to_tuples} \t\t  type is {type(str_to_tuples)}")
print(f"{str_to_list} \t\t  type is {type(str_to_list)}")
print(f"{str_to_set} \t\t  type is {type(str_to_set)}")


dict_str = {"a":1}
print(f"{dict_str} \t\t  type is {type(dict_str)}")




s = "12345678"
str_to_tuples = tuple(s)
str_to_list = list(str_to_tuples)
str_to_list.append(9)
str_to_set = set(str_to_list)
str_to_set.add(10)
print(f"{str_to_tuples} \t\t  type is {type(str_to_tuples)}")
print(f"{str_to_list} \t\t  type is {type(str_to_list)}")
print(f"{str_to_set} \t\t  type is {type(str_to_set)}")


print("-------------------------------------------------------------------------------------")
print("其他显式转换")
num = 98
num_to_char = chr(num)
char_to_num = ord(num_to_char)
num_to_hex = hex(char_to_num)
num_to_oct = oct(num)

print(f"{num} \t\t  type is {type(num)}")
print(f"{num_to_char} \t\t  type is {type(num_to_char)}")
print(f"{char_to_num} \t\t  type is {type(char_to_num)}")
print(f"{num_to_hex} \t\t  type is {type(num_to_hex)}")
print(f"{num_to_oct} \t\t  type is {type(num_to_oct)}")