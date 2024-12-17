#!/usr/bin/env python3

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    if(counter % 10 == 0):
        print(f"{sum} ==> {counter}")
print("1 到 %d 之和为: %d" % (n, sum))