def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Memilih elemen untuk memasukkan ke bagian yang sudah diurutkan
        j = i - 1
        
        # Memindahkan elemen yang lebih besar dari key ke posisi yang lebih tinggi
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Memasukkan elemen key ke dalam bagian yang sudah diurutkan

# Contoh penggunaan
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)

print("Hasil setelah pengurutan:")
for i in range(len(arr)):
    print(arr[i])
