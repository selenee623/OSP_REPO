#!/usr/bin/python

def binoct(a):		# 2 -> 8
	b = int(a, 2)
	return format(b, 'o')


def bindec(a):		# 2 -> 10
	b = int(a, 2)
	return b

def binhex(a):		# 2 -> 16
	b = int(a, 2)
	return format(b, 'x').upper()
