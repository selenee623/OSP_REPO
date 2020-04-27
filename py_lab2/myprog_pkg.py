#!/usr/bin/python
import my_pkg

if __name__ == '__main__':
	while True:
		n = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))
	
		if(n == 1):
			num = input("input binary number : ")
			print("=> OCT>", my_pkg.binoct(num))
			print("=> DEC>", my_pkg.bindec(num))
			print("=> HEX>", my_pkg.binhex(num))

		if(n == 2):
			stra = input("1st list: ")
			strb = input("2nd list: ")

			print("=> union ", my_pkg.unionset(stra, strb))
			print("=> intersection ", my_pkg.interset(stra, strb))

		if(n == 3):
			print("exit the program")
			break	
