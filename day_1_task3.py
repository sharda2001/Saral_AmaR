num=int(input('enter the number'))
num1=int(input('enter the number'))
for num in range(num,num1+1): 
    s=0
    temp=num
    while temp>0:
	    digit=temp%10
	    s+=digit**3
	    temp//=10
    if num==s:
	    print(num,' armstrong number',)
