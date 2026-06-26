class solution:#26/06/2026
    def checksort(self,arr):
        n=len(arr)
        i=0
        for j in range(1,n):
            if arr[i]!=arr[j]:
                i+=1
                arr[i]=arr[j]
        return i+1
#arr=[0,0,3,3,5,6]
# in=[0,1,2,3,4,5]

# i=0 and j=1 
#are they equal ,yes ...python skips it
#now only j moves not i 
#i=0 and j=2 ...0 and 3 
#are they equal no : enter if and excutes 2 lines
#i moves
#then copies 3 new number to i 
#now its in=1,0 and in=2,3 
