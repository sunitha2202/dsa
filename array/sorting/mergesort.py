# merge sorting will remove duplicates
class Solution:
    def mergeSort(self,list1,m,list2,n):
        
        list3=[]
        i,j=0,0
        while i<m and j<n:
            if list1[i]<list2[j]:
                if not list3 or list3[-1] != list1[i]:
                    list3.append(list1[i])
                    i+=1
            elif list1[i]>list2[j]:
                 if not list3 or list3[-1] != list2[j]:
                     list3.append(list2[j])
                     j+=1
            else:  # list1[i] == list2[j]
                if not list3 or list3[-1] != list1[i]:
                    list3.append(list1[i])
                i += 1
                j += 1
           
        while i<m:
            
            if not list3 or list3[-1]!= list1[i]:
                list3.append(list1[i])
                i+=1
        while j<n:
            if not list3 or list3[-1]!= list2[j]:
                list3.append(list2[j])
                j+=1
        return list3
sol=Solution()
list1=[1,2,4]
list2=[1,3,4]
m=3
n=3
print(sol.mergeSort(list1,m,list2,n))


