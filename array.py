arr = [1,2,3,4,5,522,56,2,5,6]
print(len(arr))
# Secon larget elemnet
print("Second Largest")
first = arr[0]
second = arr[0]
for i in arr:
    if i >= first:
        second = first
        first = i
    if i < first and i > second:
        second = i

print(second)

# Reverse the array and store into the new array
print("Reverse Array:")
# 1
print(arr)
reversed = []
for i in range(len(arr)-1,-1, -1):
    reversed.append(arr[i])

# 2
print(reversed)
reversed.reverse()
print(reversed)

#3
n = 10
rev = [i for i in range(n) ]
print(rev)

#4
n = 10
rev = [arr[i] for i in range(n-1,-1, -1)]
print(rev)

#5 
rev = arr[::-1]
print(rev)

#6 
for i in range(n//2):
    # Swap
    rev[i],rev[n-i-1]=rev[n-i-1],rev[i]

# 7
left = 0
right = int(len(rev)-1)
print(right)
while left<right:
    arr[left], arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(arr)



# Rotate the array
print("array rotation")
# 1
arr = [1,2,3,4,5,522,56,2,5,6]
k=1
n=len(arr)
first=arr[0]
for i in range(n-1):
    arr[i]=arr[i+1]
arr[n-1]=first
print(arr)

# 2
arr = [1,2,3,4,5,522,56,2,5,6]
first=arr[0]
arr.pop(0)
arr.append(first)
print(arr)

# 2
arr = [1,2,3,4,5,522,56,2,5,6]
k=3
first=arr[:k:]
for i in range(k,n):
    arr[i-k]=arr[i]
for i in range(k):
    arr[n-k+i]=first[i]
print(first)
print(arr)

# 3
arr = [1,2,3,4,5,522,56,2,5,6]
for j in range(k):
    first=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=first

print(arr)

# 4
arr = [1,2,3,4,5,522,56,2,5,6]
k=3
rotated = [0] * n
for i in range(k,n+k):
    rotated[i-k]=arr[i%n]
print(rotated) 

# 5 Best
def reverse(arr,left,right):
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
arr = [1,2,3,4,5,522,56,2,5,6]
k=3
arr.reverse()
reverse(arr,0,n-k-1)
reverse(arr,n-k,n-1)

print(arr)

# give the array of zero's and one's find the longest consecutive sequ of eiterh of 1 or zeros
print("# give the array of zero's and one's find the longest consecutive sequ of eiterh of 1 or zeros")
arr = [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1]
n=len(arr)
max_z=0 if arr[0] else 1
max_o=arr[0]
max_num=1
current=arr[0]
count=1
for i in range(1,n):
    if arr[i]==arr[i-1]:
        count+=1
        max_num=max(max_num,count)
        if current==1:
            max_o = max(max_o,count)
        
        elif current==0:
            max_z = max(max_z,count)
        
    else:
        count=1
        current=arr[i]
print(max_z,max_o, max_num)
            
# Given an array of integer, put all the 1s to the end while mantaing the relative position of all other elements
print("# Given an array of integer, put all the 1s to the end while mantaing the relative position of all other elements")
arr = [12,12,3,1,3,1,1,1,32,1,32,1,1,432,1]
print(arr)
n = len(arr)
one=0
for index, i in enumerate(arr):
    if i !=1:
        arr[one]=i
        one+=1
for i in range(one,n):
    arr[i]=1
print(arr)

# Given an array of integer, reverse the array in groups of K
print("Given an array of integer, reverse the array in groups of K")
arr = [12,12,3,1,3,1,1,1,32,1,32,1,1,432,1]
print(arr)
n = len(arr)
k=3
for i in range(0,n,k):
    reverse(arr,i,i+k-1)
print(arr)

# Find the array of distinct integer find the 3rd Third smallest element in it
print("# Find the array of distinct integer find the 3rd Third smallest element in it")
arr =  [12,12,3,1,3,1,1,1,32,1,32,1,1,432,1]
print(arr)
n = len(arr)
k=3

first=second=last=1000

for i in arr:
    if i <first:
        last=second
        second=first
        first=i
    elif i < second and i > first:
        last=second
        second=i
    elif i < last and i >second:
        last = i

print(last)