a=1
while True:
    if a==1 : 
        array = input("enter your array like 1,2,3,4,5 \n")
        list = array.split(",")
        length = len(list)
        x = 0

        for i in range(length):

            if list[i] == list[length - 1]:
                x= 1

            else :
                x = 0
                break

            length -= 1


        if x == 0:
            print(" is not symmetrical.")
        if x == 1:
            print(" is symmetrical.")

        a=int(input("\n again ? yes = enter 1 , no =enter 2  "))

        if a==2:
            print("finish")
            exit()    