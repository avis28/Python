def remainder(st) :
	
	
	ln = len(st)
	
	rem = 0
	
	
	for i in range(0, ln) :
		num = rem * 10 + (int)(st[i])
		rem = num % 11
		
	return rem
st = input()
print(remainder(st))

