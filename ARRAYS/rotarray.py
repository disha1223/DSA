class solution:
    #26/06/2026 ,rotate array by one
    def rotarray(self,arr):
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]#shift everything left
        arr[-1]=temp#add at the end