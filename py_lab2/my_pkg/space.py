#!/usr/bin/python

def unionset(stra, strb):
	sa = stra.strip('[]')
	sa = sa.replace(' ', '')

	lista = list(map(int, sa.split(",")))

	sb = strb.strip('[]')
	sb = sb.replace(' ', '')

	listb = list(map(int, sb.split(",")))

	seta = set(lista)
	setb = set(listb)

	listu = list(seta.union(setb))
	
	return listu

def interset(stra, strb):
	sa = stra.strip('[]')
	sa = sa.replace(' ', '')

	lista = list(map(int, sa.split(",")))

	sb = strb.strip('[]')
	sb = sb.replace(' ', '')

	listb = list(map(int, sb.split(",")))

	seta = set(lista)
	setb = set(listb)

	listi = list(seta.intersection(setb))

	return listi
