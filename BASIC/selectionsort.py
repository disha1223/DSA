arr=[5,2,4,1,3]
n=len(arr)

for i in range(n):
    min=i #set 1st ele=smallest
    for j in range(i+1,n): #tart from 1 
        if arr[j]<arr[min]: #compare with 2nd
            min=j
    arr[i],arr[min]=arr[min],arr[i] #swap

print(arr)
