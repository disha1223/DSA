class solution: #25/06/2026

    def second(self,arr):
        largest=arr[0]
        second=-1

        for i in arr:
            if i>largest:
                largest=i
            elif i>second and i!=largest:
                second= i

        return second

            