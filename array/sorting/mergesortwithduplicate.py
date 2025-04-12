# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, list1,m, list2,n):
        list3=[]
        i,j=0,0
        while i<m and j<n:
            if list1[i]<list2[j]:
                list3.append(list1[i])
                i+=1
            else:# list1[i]>list2[j]:
                list3.append(list2[j])
                j+=1
           
        while i<m:
            list3.append(list1[i])
            i+=1
        while j<n:
            list3.append(list2[j])
            j+=1
        return list3
        
sol=Solution()
list1=[1,2,4]
list2=[1,3,4]
m=3
n=3
print(sol.mergeSort(list1,m,list2,n))