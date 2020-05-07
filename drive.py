country = input("input your country(台灣/美國):")
age = input("inprt your age:")
age = int(age)

if country == "台灣":
	if age >= 18:
		print("你可以考駕照")
	else :
		print("你還不可以考駕照")
elif country == "美國":
	if age >= 16:
		print("你可以考駕照")
	else:
		print("你還不可以考駕照")
		