#25/06/2026


class solution:
    def maj(self,arr):
        n=len(arr)
        count={}

        for i in arr:           # i is the element not index...
            count[i]=count.get(i,0)+1

        for i in arr:
            if count[i]>n//2:
                return i
    