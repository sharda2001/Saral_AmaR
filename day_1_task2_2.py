user=int(input("enter the number "))
i=0
while i<= user:
    if user%2==0:
        print(user)
        a=user-2
        b=a-2
        print(a)
        print(b)
        break    
    elif user%2!=0:
        print(user)
        a=user+2
        b=a+2
        print(a)
        print(b)
        break
    i=i+1