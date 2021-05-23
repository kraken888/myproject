def myproject(a,b):
	try:
		int(a)
		float(b)
	except:
		print("Something went wrong")
	return a,b
