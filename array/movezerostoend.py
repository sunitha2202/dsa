class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
n=len(arr)
j=0
for i in range(len(arr)):
    	    if arr[i]!=0:
    	        arr[j]=arr[i]
    	        j+=1
    	for i in range (j,len(arr)):
    	    arr[i]=0
    	return arr