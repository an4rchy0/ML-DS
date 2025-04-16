from itertools import combinations
data = {
    'province': ['Aceh', 'Aceh', 'Jakarta', 'Jakarta', 'Jabar', 'Jabar', 'Jabar', 'Jateng', 'Jateng', 'Kalbar'],
    'citiesReg': ['Banda Aceh', 'Sabang', 'Jakarta Timur', 'Jakarta Selatan', 'Bogor', 'Sukabumi', 'Bandung', 'Semarang', 'Brebes', 'Pontianak'],
    'poor%': [7.61, 15.32, 4.28, 3.56, 8.13, 7.7, 7.15, 7.82, 17.43, 5.18],
    'regGDP': [18.28, 1.53, 470.99, 644.57, 236.14, 67.39, 123.04, 49.03, 47.14, 8.54],
    'lifeExp': [71.47, 70.50, 74.48, 74.22, 71.38, 71.2, 73.73, 75.84, 69.54, 71.09],
    'avgSchoolTime': [12.83, 11.18, 11.67, 11.64, 8.31, 7.1, 9.07, 8.03, 6.22, 7.04],
    'expPercap': [16891, 11378, 17733, 23888, 10410, 8850, 10307, 12070, 10152, 7758]
}

def BSAsc(data):
    n = len(data['poor%'])
    for i in range(n - 1): # Iterasi melalui setiap elemen, kecuali elemen terakhir
        for j in range(0, n - i - 1): # Iterasi melalui elemen yang belum terurut
            if data['poor%'][j] > data['poor%'][j + 1]: # Membandingkan elemen saat ini dengan elemen berikutnya
                for key in data: # Melakukan pertukaran nilai untuk semua key di dalam data
                    data[key][j], data[key][j + 1] = data[key][j + 1], data[key][j]

    for i in range(len(data['province'])):
        print(f"{data['province'][i]} - {data['citiesReg'][i]} - {data['poor%'][i]}")
def BSDesc(data):
    n = len(data['poor%'])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data['poor%'][j] < data['poor%'][j + 1]:  
                for key in data:
                    data[key][j], data[key][j + 1] = data[key][j + 1], data[key][j]

    for i in range(len(data['province'])):
        print(f"{data['province'][i]} - {data['citiesReg'][i]} - {data['poor%'][i]}")

def BFSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

def BFCombination(arr, target_sum):
    for r in range(0, len(arr)):
        for c in combinations(arr, r):
            if sum(c) == target_sum:
                return c
    return None

oop = True
while(oop) :
    print('\tAlgoritma Brute Force')
    print('1.Bubble Sort 2.Brute Force')
    ops = int(input('\nYour Choice : '))
    if ops == 1 :
        print('1.Ascending 2.Descending')
        bs = input('Your Choice')
        if bs == '1' :
            BSAsc(data)
        elif bs == '2' :
            BSDesc(data)
        else :
            print('Incorect Ops!')
    elif ops == 2 :
        print('1.Searching 2.Combination')
        bf = input('Your Choice : ')
        if bf == '1' :
            prv = input('Name of Cities Region you want to Search : ')
            index = BFSearch(data['citiesReg'], prv) 
            if index != -1:
                print(f"{prv} found at index {index}")
                print(f"{data['province'][index]} - {data['citiesReg'][index]} - {data['poor%'][index]}")
            else:
                print(f"{prv} not found in citiesReg")
        elif bf == '2' :
            bfdata = []
            for i in range(len(data)) :
                data_item = input('Enter data item : ')
                bfdata.append(int(data_item))
                i += 1
            tr = int(input('Enter target number: '))
            result = BFCombination(bfdata, tr)
            if result:
                print(f"Combination for result {tr} : {result}")
            else:
                print("Tidak ditemukan kombinasi yang sesuai.")
        else :
            print('Incorect Ops!')
    else :
        print('ops doesnt correctly!')

    oop = input('Want to play again? (true/false) : ').lower() == 'true'
    print('\n\n')