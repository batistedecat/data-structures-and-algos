def zoek_index(arr: list, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def komt_voor(arr, vals):
    ans = []
    for val in vals:
        ans.append(False if zoek_index(arr, val) == -1 else True)
    return ans

def eerste_groter(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left if left < len(arr) else -1


if __name__ == "__main__":
    arr = [3, 7, 11, 19, 25, 40, 41, 99]
    vals = [3, 7, 10, 18, 11, 19, 25, 56, 66, 99]
    print(zoek_index(arr, 7))
    print(zoek_index(arr, 3))
    print(zoek_index(arr, 11))
    print(zoek_index(arr, 40))
    print("\n")
    print(zoek_index(arr, 42))
    print(komt_voor(arr, vals))
    print(eerste_groter(arr, 99))
    print(eerste_groter(arr, 41))
    print(arr[eerste_groter(arr, 41)])
