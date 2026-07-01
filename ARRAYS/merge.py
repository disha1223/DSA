class solution:
    def merge(self,arr1,arr2):
        ans=[]
        for i in range(len(arr1)):
            if arr1[i] not in ans:
                ans.append(arr1[i])
        for i in range(len(arr2)):
            if arr2[i] not in ans:
                ans.append(arr2[i])

        ans.sort()
        return ans
    #2/07/2026-12.45 A.M 