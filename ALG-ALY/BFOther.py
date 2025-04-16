def brute_force_string_search(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    
    return -1

# Contoh penggunaan
text = "algorithm is amazing"
pattern = "is"
index = brute_force_string_search(text, pattern)

if index != -1:
    print(f"Pattern ditemukan pada indeks ke-{index}.")
else:
    print("Pattern tidak ditemukan.")
