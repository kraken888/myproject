def myproject(a,b):
	try:
		float(a)
		float(b)
	except:
		print("Something went wrong")
	return a,b
