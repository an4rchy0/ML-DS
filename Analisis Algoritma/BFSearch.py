def brute_force_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan indeks jika target ditemukan
    
    return -1  # Mengembalikan -1 jika target tidak ditemukan

# Contoh penggunaan
my_list = [5, 9, 3, 7, 2, 8, 4]
search_target = 7

result = brute_force_search(my_list, search_target)

if result != -1:
    print(f"Target ditemukan di indeks ke-{result}.")
else:
    print("Target tidak ditemukan dalam list.")
