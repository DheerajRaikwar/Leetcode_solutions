def minimumShot(points):
    arrow=0
    i=0
    j=1
    for k in len(points):
        if j!=len(points):
            while points[i]<points[j]:
            	i+=1
                j+=1
            arrow+=1
    return arrow
 

N =int(input())
Hi = list(map(int,input().strip().split()))[:N]
print(minimumShot(Hi))
