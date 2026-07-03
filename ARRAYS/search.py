class solution:
    def search(self,arr,x):
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1
    #2/07/2026-12.45 A.M 