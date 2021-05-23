def myproject(a,b,c):
	try:
		float(a)
		float(b)
		float(c)
	except:
		print("Something went wrong")
	return a,b,c
