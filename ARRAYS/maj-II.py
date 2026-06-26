#25/06/2026

class solution:
    def majii(self,arr):
        count={}
        n=len(arr)
        ans=[]

        for  i in arr:
            count[i]=count.get(i,0)+1

        for i in count:
            if count[i]>n//3:
                ans.append(i)
        return ans 