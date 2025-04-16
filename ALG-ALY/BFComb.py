from itertools import combinations

def find_combination_sum(arr, target_sum):
    for r in range(1, len(arr) + 1):
        for combination in combinations(arr, r):
            if sum(combination) == target_sum:
                return combination
    
    return None

# Contoh penggunaan
my_numbers = [10, 20, 30, 40, 50]
target = 70
result = find_combination_sum(my_numbers, target)

if result:
    print(f"Kombinasi yang menghasilkan {target}: {result}")
else:
    print("Tidak ditemukan kombinasi yang sesuai.")
