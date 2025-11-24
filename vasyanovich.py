# surname.py
# Replace "surname" with your real surname in the file name


def bubble_sort(arr):
    n = len(arr)
    a = arr.copy()

    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a



def selection_sort(arr):
    a = arr.copy()

    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a



def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
    return a



if __name__ == "__main__":
    nums = [5, 3, 8, 4, 2]
    print("Bubble Sort:", bubble_sort(nums))
    print("Selection Sort:", selection_sort(nums))
    print("Insertion Sort:", insertion_sort(nums))
