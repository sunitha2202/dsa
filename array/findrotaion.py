class Solution:
    def findKRotation(self, arr):
        # code here
        left=0
        right = len(arr)-1
        while left< right:
            mid=(left+right)//2
            if arr[mid]>arr[right]:
                left = mid+1
            else:
                right=mid
        return left
sol=Solution()
arr=[6,5,1,2,3,4]
print(sol.findKRotation(arr))