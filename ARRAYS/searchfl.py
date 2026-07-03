class solution:
    def first(self,arr,target):
        ans=-1
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==target:
                ans=mid
                high=mid-1

            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return ans 
    
    def last(self,arr,target):
        ans=-1
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==target:
                ans=mid
                low=mid+1

            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return ans 
                     
    def searcfl(self,arr,target):
        first=self.first(self,arr,target)
        last=self.last(self,arr,target)
        return [first,last]
#3/07/2026