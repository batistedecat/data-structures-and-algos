def merge(arr1, arr2):
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res

def mergesort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    rigth = mergesort(arr[mid:])
    return merge(left, rigth)

if __name__ == "__main__":
    arr1 = [45, 12, 23, 47, 72, 49, 18, 78]
    arr2 = [12, 18, 23, 45, 47, 49, 72, 78]
    ls = [i for i in range(0, 20, 2)]
    arr = [i for i in range(1, 20, 3)]
    print(merge(ls, arr))
    print(mergesort(arr1))