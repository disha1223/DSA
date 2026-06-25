class solution:
    def maj(self,arr):
        n=len(arr)
        count={}

        for i in arr:
            count[i]=count.get(i,0)+1

        for i in arr:
            if count[i]>n//2:
                return i
    