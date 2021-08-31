# user=input('enter the string ')
# list=['i','n','g']
# i=0
# while i<len(user):
#     if user[i] not in list:
#         print(user[i],end="")
#         print("ing")
#     elif user[i] in list:
#         print(user[i],end="")
#         print('ly')
#     elif user[i]=="ly":
#         print(user)
#     else:
#         i=i+1

user=input("enter the string ")
i=0
while i<len(user):
    if user[i]=="ing":
        print(user[i],end="")
        print("ly")
    # elif user[i]!="ing":
    #     print(user,end="")
    #     print("ing")
    # else:
    #     print("nnnn")
    i+=1


    