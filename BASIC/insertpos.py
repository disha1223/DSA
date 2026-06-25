n=int(input("enter size:"))

arr=[]

for i in range(n):
    num=int(input(f"enter element {i+1}:"))
    arr.append(num)

ele=int(input("enter to insert:"))
pos=int(input("enter psotion:"))

arr.insert(pos,ele)
for i in range(len(arr)):
    print(arr[i],end="")