n = int(input())                      # read the count
arr = list(map(int, input().split())) # read the array on one line

largest = arr[0]
second = -1

for i in arr[1:]:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)

#5/08/2026