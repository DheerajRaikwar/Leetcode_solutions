T=int(input())
while(T):
    x,y=map(int,input().split())
    A=x+y    
    if A%x!=0:
        if A%y!=0:
            print(1)
    else:
        print(0)
        
        
        
        
