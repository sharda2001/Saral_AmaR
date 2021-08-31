st=input("enter tha any name ")
i=0
s=" "
while i<=len(st):
		if i==0:
			s=s+st[i]
		if i==1:
			s=s+st[i]	
			s=s+st[-2]
			s=s+st[-1]			
		i=i+1				
print(s)
