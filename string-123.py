
# Count prequecy
print("Count Frequency of character:")
freq = {}
string = "rasdfasdfasdfdfasdfavi"
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)

# Palindrome
print("Palindrome")

s1="abccb22a"
left=0 
right=len(s1)-1

flag=True
while(left<right):
    if s1[left] != s1[right]:
        print("Not Palindrome")
        flag=False
        break

    left+=1
    right-=1

if flag:
    print("It is Palindrome")


# Reverse
print("Reverse")
s1="abccb22a"
left=0 
print(s1[::-1])

if flag:
    print("It is Palindrome")