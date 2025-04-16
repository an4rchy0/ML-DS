def brute_force_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]  # Melakukan pertukaran jika tidak terurut

# Contoh penggunaan
my_list = [64, 25, 12, 22, 11]
brute_force_sort(my_list)
print("Hasil pengurutan:")
print(my_list)
