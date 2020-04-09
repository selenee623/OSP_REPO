#!/usr/bin/python

n = int(input("fibonacci number? "))

def fibo(n):
  list = []
  for i in range(0, n):
    if i < 2:
      list.append(1)
    else:
      list.append(list[i-1] + list[i-2])
  print(", ".join(map(str, list)))
  return list[n-1]

print("F%d = %d" % (n, fibo(n)))
