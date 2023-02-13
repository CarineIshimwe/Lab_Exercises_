def graduate(a):
    if a==120:
        print('dear undergraduate  you have enough credits for graduation')
    else:
        print('dear undergraduate  you do not have enough credits for graduation')

def post_graduate(b):
    if b==60:
        print('dear post_graduate  you have enough credits for graduation')
    else:
        print('dear post_graduate  you do not  have enough credits for graduation')
while True:
    print("1. graduate")
    print("2. post_graduate")
    print("3. Exit")
    choice = int(input("\nEnter your Choice(1-3): "))
    if choice == 1:
        a = int(input('enter your credits :'))
        graduate(a)
    elif choice == 2:
        b = int(input('enter your credits:'))
        post_graduate(b)
    elif choice == 3:
        break
    else:
        print("Please Provide a valid Input!1")




