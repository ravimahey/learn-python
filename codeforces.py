

t=int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    a=[int(i) for i in input().split(" ")]
    diff={}
    flag=0
    for i in range(m):
        bi,ci = map(int,6+ input().split())
        if bi-1 in  diff:
            sum = a[bi-1] + diff[bi-1] + ci 
            
    for i in range(n):
        print(a[i],end=" ")
    print()




"""
t=int(input())
for _ in range(t):
    n, h, l = map(int, input().split())
    a=[int(i) for i in input().split(" ")]
    count=0
    a.sort()
    left=0
    right=n-1
    while(left<right):
        if a[left]<=h and a[right]<=l:
            left+=1
            right-=1
            count+=1
        elif a[left]<=l and a[right]<=h:
            left+=1
            right-=1
            count+=1
        elif a[right]>h:
            right-=1
        elif a[right]>l:
            right-=1

    print(count)

"""    
    