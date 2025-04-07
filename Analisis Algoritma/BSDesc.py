data = {
    'province': ['Aceh', 'Aceh', 'Jakarta', 'Jakarta', 'Jabar', 'Jabar', 'Jabar', 'Jateng', 'Jateng', 'Kalbar'],
    'citiesReg': ['Banda Aceh', 'Sabang', 'Jakarta Timur', 'Jakarta Selatan', 'Bogor', 'Sukabumi', 'Bandung', 'Semarang', 'Brebes', 'Pontianak'],
    'poor%': [7.61, 15.32, 4.28, 3.56, 8.13, 7.7, 7.15, 7.82, 17.43, 5.18],
    'regGDP': [18.28, 1.53, 470.99, 644.57, 236.14, 67.39, 123.04, 49.03, 47.14, 8.54],
    'lifeExp': [71.47, 70.50, 74.48, 74.22, 71.38, 71.2, 73.73, 75.84, 69.54, 71.09],
    'avgSchoolTime': [12.83, 11.18, 11.67, 11.64, 8.31, 7.1, 9.07, 8.03, 6.22, 7.04],
    'expPercap': [16891, 11378, 17733, 23888, 10410, 8850, 10307, 12070, 10152, 7758]
}

def bubble_sort_descending(data):
    n = len(data['poor%'])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data['poor%'][j] < data['poor%'][j + 1]:  
                for key in data:
                    data[key][j], data[key][j + 1] = data[key][j + 1], data[key][j]

bubble_sort_descending(data)

for i in range(len(data['province'])):
    print(f"{data['province'][i]} - {data['citiesReg'][i]} - {data['poor%'][i]}")
