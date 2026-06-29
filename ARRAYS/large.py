#25/06/2026
class solution:
    def large(self,arr):
        large=arr[0]
        for i in arr:
            if i>large:
                large=i
        return large