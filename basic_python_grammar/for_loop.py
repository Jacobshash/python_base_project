sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)
print()

word = 'runoob'
for letter in word:
    print(letter)

print()
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(f"range(1, 6) ==> {number}")


print()
for number in range(1, 6, 2):
    print(f"range(1, 6, 2) ==> {number}")



print()
for number in range(0, 6, 2):
    print(f"range(0, 6, 2) ==> {number}")


print()
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in range(len(sites)):
    print(f"循环数据 {site} ==> {sites[site]}")


print()
runoob = "Runoob"
for x in range(len(runoob)):
    print(f"range('Runoob') {x} ==> {runoob[x]}")


print()
for x in range(6):
    print(f"range(6) ==> {x}")
else:
    print("Finally finished!")


print()
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
