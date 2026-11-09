def quicksort(bedragen):
    if len(bedragen) <=1:
        return bedragen
    pivot = bedragen[0]
    left = [val for val in bedragen if val < pivot]
    equal = [val for val in bedragen if val == pivot]
    right = [val for val in bedragen if val > pivot]
    return quicksort(left) + equal + quicksort(right)

def quicksort_willekeurig(bedragen):
    from random import randrange
    if len(bedragen) <=1:
        return bedragen
    pivot = bedragen[randrange(len(bedragen))]
    left = [val for val in bedragen if val < pivot]
    equal = [val for val in bedragen if val == pivot]
    right = [val for val in bedragen if val > pivot]
    return quicksort_willekeurig(left) + equal + quicksort_willekeurig(right)


def quicksort_mid(bedragen):

    if len(bedragen) <=1:
        return bedragen
    mid = len(bedragen)//2
    pivot = bedragen[mid]
    left = [val for val in bedragen if val < pivot]
    equal = [val for val in bedragen if val == pivot]
    right = [val for val in bedragen if val > pivot]
    return quicksort_mid(left) + equal + quicksort_mid(right)

if __name__ == "__main__":
    import random
    print(quicksort([450, 120, 980, 300, 120, 760, 888, 645, 1000]))
    print(quicksort_willekeurig(list(range(200))))
