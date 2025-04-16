import cv2
import os

input_folder = r'D:\(D) Document\Project\Python\ML\CVCropFace\path\to\faceF'
output_folder = r'D:\(D) Document\Project\Python\ML\CVCropFace\path\to\outputFlip3'

# Membuat folder output jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Mendapatkan daftar file dalam folder input
files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

# Memproses setiap file gambar dalam folder input
for idx, file in enumerate(files, start=1):
    img = cv2.imread(os.path.join(input_folder, file))
    
    if img is None:
        continue

    # Memutar gambar 90 derajat berlawanan arah jarum jam
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # Menentukan nama file output dengan format "gge{idx}_2.png"
    output_name = f"ggl{idx}_2.png"
    
    # Menyimpan gambar yang sudah diputar ke dalam folder output
    output_path = os.path.join(output_folder, output_name)
    cv2.imwrite(output_path, rotated_img)

print(f"Semua gambar dari folder '{input_folder}' telah berhasil diputar 90 derajat berlawanan arah jarum jam dan disimpan di folder '{output_folder}' dengan format nama yang baru.")
