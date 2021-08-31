num=int(input("enter the number"))
num2=int(input("enter the number"))
for num in range(num,num2+1):  
    sum=0
    i=1
    while i<num:
	    if num%i==0:
		    sum=sum+i
	    i=i+1
    if sum==num:
	    print(num,'perfect number')
    
