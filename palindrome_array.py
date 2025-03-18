arr=[1,2,4,6,34,4]
rev_arr=[]
for i in range(len(arr)-1,-1,-1):
    rev_arr.append(arr[i])
if rev_arr == arr:
    print("true")
else:
    print("false")