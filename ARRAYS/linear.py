class solution:
    #26/06/2026
    def search(self,arr,target):
        n=len(arr)
        for i in range(n):
            if arr[i]==target:
                return i
        return -1