year=int(input('enter the year '))
if year%4==0:
	print("leap year")
	if year%100==0:
		print('century year')
	if year%400==0:
		print('century leap year')
else:
	print('leap year')

# year=int(input("enter your year"))
# if year %4==0:
# 	if year%100==0:
# 		if year%400==0:
# 			print("sentury leap year")
# 		else:
# 			print("sentuary leap year nhi hai")
# 	else:
# 		print("century year")
# else:
# 	print("leap year")

  
