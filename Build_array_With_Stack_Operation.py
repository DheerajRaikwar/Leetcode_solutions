#def buildArray(target,n):
target = [1,3]
k = 0
narr=[i for i in range(1,5)]
n= len(narr)
arr =[]
for j in range(n):
    arr.append("Push")
    if narr[j] in target:
        pass    
    else:
        arr.append("Pop")
print(arr)


    
    
'''
n=3
target= [1,3]
print(*buildArray(target,n))
'''


