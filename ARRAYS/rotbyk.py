class Solution:
    def rotateArray(self, arr, k: int) -> None:
        n=len(arr)
        k=k%n
        arr[:]=arr[k:]+arr[:k]