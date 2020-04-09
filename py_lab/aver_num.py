#!/usr/bin/python

#1
n = int(input("How many numbers will you enter? : "))

num = 0
sum = 0
ave = 0

for i in range(n):
  num = int(input())  #2
  sum += num          #3

ave = sum/n           #4
print(ave)            #5
