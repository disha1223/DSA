class solution:
    def lower(self,arr,target):
        
        for i in range(len(arr)):
            if arr[i]<=target:
                return i
        return len(arr)
    #2/07/2026-12.45 A.M 