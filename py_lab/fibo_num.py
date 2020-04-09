#!/usr/bin/python

n = int(input("fibonacci number? "))      #1

def fibo(n):
  list = []
  for i in range(0, n):
    if i < 2:
      list.append(1)                      #F1 = F2 = 1
    else:
      list.append(list[i-1] + list[i-2])  #F(n) = F(n-1) + F(n-2)
  print(", ".join(map(str, list)))        #2
  return list[n-1]

print("F%d = %d" % (n, fibo(n)))          #3
