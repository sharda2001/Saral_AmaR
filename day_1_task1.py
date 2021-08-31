num1= int(input("Enter the num1:"))
num2 = int(input("Enter the num2:"))
for i in range(num1, num2+1):
   if((i%3==0) or (i%5==0)):
      print(i)