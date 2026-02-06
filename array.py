arr = [  1,2,3,4,5,522,56,2,5,6]

# Secon larget elemnet
first = arr[0]
second = arr[0]
for i in arr:
    if i >= first:
        second = first
        first = i
    if i < first and i > second:
        second = i

print(second)