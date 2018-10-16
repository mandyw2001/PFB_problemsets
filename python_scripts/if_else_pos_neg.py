#!/usr/bin/env python3
import sys

number = int(sys.argv[1])
if number >0 : 
	print("Positive")
	if number < 50:
		print("The number is less than 50")
		if number%2==0:
			print ("It is an even number that is smaller than 50")
	elif number >50: 
		if number%3==0:
			print ("It is larger than 50 and divisble by 3")
elif number ==0 : 
	print("The number is equal to 0")
else: 
	print("Negative")
