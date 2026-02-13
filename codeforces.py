# https://codeforces.com/problemset/problem/2179/C
import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted([int(_) for _ in input().split()])
    print(max(a[0], a[1]-a[0]))


# https://codeforces.com/problemset/problem/2182/A
# t = int(input())
# for _ in range(t):
#     n=int(input())
#     s=input()
#     if s.find("2026") >-1:
#         print(0)
#     elif s.find("2025") >-1:
#         print(1)
#     else:
#         print(0)
    # if s.find('2026'):
    #     print('2026')
    # elif s.find('2025')!=1:
    #     print(1)
    # else:
    #     print(0)
        
        
# t = int(input())

# for _ in range(t):
#     n = map(int, input().split())
#     a=[int(i) for i in input().split(" ")]
#     a.sort()
#     n=len(a)
#     counter=1
#     ans=1
    
#     for i in range(n-1):
#         if a[i]==a[i+1]:
#             continue
#         if a[i+1]-a[i]>1:
#             ans=max(ans,counter)
#             counter=1
#         else:
#             counter+=1

    

    # print(max(ans,counter))
    
    
#     original_vec = vec[:]
    
#     last_element_update = [-1] * n
#     last_reset = -1
#     reset_count=0
#     for i in range(m):
#         a, b = map(int, input().split())
#         a -= 1
        
#         if last_element_update[a] < last_reset:
#             vec[a] = original_vec[a]
        
#         vec[a] += b
        
#         if vec[a] > h:
#             last_reset = i
#             reset_count+=1
#             vec[a]=original_vec[a]
#         last_element_update[a] = i
    
#     for i in range(n):
#         if last_element_update[i] < last_reset:
#             vec[i] = original_vec[i]
    
#     print(*vec)

        
# t = int(input())
# for _ in range(t):
#     n, m, h = map(int, input().split())
    
#     a = [0] + list(map(int, input().split()))
#     original = a.copy()
    
#     last_updated = [-1] * (n + 1)
#     last_crash = -1
    
#     for i in range(m):
#         bi, ci = map(int, input().split())

#         if last_updated[bi] < last_crash:
#             a[bi] = original[bi]
        
#         new_value = a[bi] + ci
        
#         if new_value > h:
#             last_crash = i
#         else:
#             a[bi] = new_value
#             last_updated[bi] = i
    
#     for i in range(1, n+1):
#         if last_updated[i] < last_crash:
#             a[i] = original[i]
    
#     print(*a[1:])




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
    