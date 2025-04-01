#selention sort
arr=[4,6,3,33,7,56,9,10]
for x in range(0,len(arr)-1,1):
    min = x
    for i in range(x+1,len(arr),1):
        if arr[i]<arr[min]:
            min=i
    temp = arr[min]
    arr[min]=arr[x]
    arr[x]=temp
print(arr)

