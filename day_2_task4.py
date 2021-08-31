user=int(input("inter the number"))
i=0
j=1
while i<=user:
    i=i+j
    j=j+i
    if i%2==0:
        print(i)
    elif j%2==0:
        print(j)
  