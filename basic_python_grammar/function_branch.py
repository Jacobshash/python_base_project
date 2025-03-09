import traceback


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# print(ask_ok('Do you really want to quit?'))
# print(ask_ok('OK to overwrite the file?', 2))
# print(ask_ok('OK TO OVERWRITE THE FILE?', 0, 'Come on, only yes or no!'))



i = 5

def f(arg=i):
    print(arg)

i = 6
f()


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l
print(f(1))
print(f(2))
print(f(3))



def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 个位置参数
parrot(voltage=1000)                                  # 1 个关键字参数
parrot(voltage=1000000, action='VOOOOOM')             # 2 个关键字参数
parrot(action='VOOOOOM', voltage=1000000)             # 2 个关键字参数
parrot('a million', 'bereft of life', 'jump')         # 3 个位置参数
parrot('a thousand', state='pushing up the daisies')  # 1 个位置参数，1 个关键字参数

print('=' * 40)
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

try:
    raise ValueError('Hello!')
except Exception as e:
    print("捕获到异常:", e)
    traceback.print_exc()


print('=' * 40)