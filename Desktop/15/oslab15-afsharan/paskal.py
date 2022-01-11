a=1
while True:
    if a==1 : 
        n = int(input("enter you number"))
        List = []
        for i in range(n):
            r = []
            if i == 0:
               r.append(1)
            else:
                for j in range(i+1):
                    if j==i or j==0 :
                        r.append(List[i-1][j-1])
                    else:
                        r.append(List[i-1][j]+List[i-1][j-1])
            List.append(r)
        for i in range(n):
            for j in range(i+1):
                print(List[i][j], end=' ')
            print()
        
        a=int(input("\n again ? yes = enter 1 , no = enter 2"))

    if a==2:
        print("finish")
        exit()