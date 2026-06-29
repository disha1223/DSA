class solution:
    def move(self,arr):
        n=len(arr)
        i=0
        for j in range(n):
            if arr[j]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1