class solution:
    def dup(self,arr):
        n=len(arr)
       
        for i in range(n-1):
            if arr[i]<arr[i+1]:
                return True
        return False 