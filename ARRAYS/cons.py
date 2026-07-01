class solution:
    def cons(self,arr):
        maxi=0
        count=0
        n=len(arr)

        for i in range(n):
            if arr[i]==1:
                count=count+1
            else:
                count=0
                maxi=max(maxi,count)
        return maxi
        #2/07/2026-12.45 A.M 