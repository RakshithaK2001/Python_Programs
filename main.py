
def binary_Search(arr,low,high,x):
    if high>=low:
        mid = high+low // 2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x
            return binary_Search(arr,low,mid-1,x)
        else:
            return binary_Search(arr,mid+1,high,x)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
a = 9
r = binary_Search(arr,0,len(arr)-1,a)
if r != -1:
    print("Index is ",r)
else:
    print("element not present in array")
