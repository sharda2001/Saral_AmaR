
user= int(input('Enter the number number : '))
reversed = 0
while(user!=0):
		r=int(user%10)
		reversed = reversed*10 + r
		user=int(user/10)
print(reversed)


