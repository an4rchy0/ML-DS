# Laporan Proyek Machine Learning - Netanel Danur Wendra

## Domain Proyek

Kemiskinan merupakan salah satu indikator penting dalam mengukur kesejahteraan masyarakat suatu wilayah. Pemerintah Indonesia terus berupaya untuk menurunkan tingkat kemiskinan melalui berbagai kebijakan pembangunan sosial dan ekonomi. Namun, tantangan besar tetap ada, terutama dalam hal memahami dan memprediksi faktor-faktor yang memengaruhi angka kemiskinan di tiap provinsi.

Dengan meningkatnya ketersediaan data sosial-ekonomi, kita kini dapat memanfaatkan pendekatan Machine Learning untuk membantu memprediksi tingkat kemiskinan suatu wilayah. Dengan pemodelan yang tepat, hasil prediksi ini dapat menjadi alat bantu pengambilan keputusan bagi pembuat kebijakan, lembaga riset, dan lembaga sosial.

Menurut Badan Pusat Statistik (BPS), faktor-faktor seperti Produk Domestik Regional Bruto (PDRB), pengeluaran per kapita, harapan hidup, dan rata-rata lama sekolah memiliki korelasi dengan angka kemiskinan. Oleh karena itu, proyek ini bertujuan untuk memprediksi persentase penduduk miskin menggunakan algoritma XGBoost Regressor berdasarkan data sosial ekonomi provinsi.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Jelaskan mengapa dan bagaimana masalah tersebut harus diselesaikan
- Jelaskan mengapa proyek ini penting untuk diselesaikan.
- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.
  
  Format Referensi: 
  - [Judul Referensi](https://scholar.google.com/) 

## Business Understanding

### Problem Statements
- Bagaimana memprediksi tingkat kemiskinan (dalam persen) di suatu provinsi berdasarkan indikator sosial-ekonomi?
- Faktor sosial-ekonomi apa yang paling berpengaruh terhadap prediksi tingkat kemiskinan menurut model?

### Goals
- Menghasilkan model prediksi kemiskinan per provinsi yang akurat.
- Mengidentifikasi fitur sosial-ekonomi yang paling berkontribusi terhadap prediksi kemiskinan.

### Solution statements
- Menggunakan algoritma XGBoost Regressor sebagai model utama karena keunggulannya dalam menangani data numerik dan hubungannya yang kompleks.
- Melakukan hyperparameter tuning untuk meningkatkan performa model.
- Melakukan eksperimen perbandingan awal dengan model baseline (misalnya Linear Regression) untuk mengevaluasi peningkatan kinerja.

## Data Understanding
Dataset ini terdiri dari data sosial ekonomi tiap provinsi di Indonesia. Dataset mencakup:
### Variabel-variabel:
- province : Nama provinsi (kategorikal)
- cities_reg : Jumlah kota/kabupaten (numerik)
- poorpeople_percentage : Persentase penduduk miskin (target/label)
- reg_gdp : Produk Domestik Regional Bruto (numerik)
- life_exp : Harapan hidup rata-rata (numerik)
- avg_schooltime : Rata-rata lama sekolah (numerik)
- exp_percap : Pengeluaran per kapita (numerik)

Dataset bersifat tabular dan numerik
Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

## Data Preparation
Tahapan yang dilakukan:
- Menghapus kolom province karena bersifat kategorikal dan tidak digunakan langsung dalam model.
- Mengecek missing values dan outlier pada setiap fitur.
- Melakukan normalisasi atau standardisasi jika diperlukan untuk model baseline.
- Melakukan feature selection untuk memastikan hanya fitur relevan yang digunakan.
- Split data menjadi training dan testing (misalnya 80:20).

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Model utama: XGBoost Regressor
XGBoost (Extreme Gradient Boosting) adalah algoritma boosting yang efisien dan akurat. Beberapa parameter yang disetel:
- n_estimators: Jumlah pohon keputusan
- max_depth: Kedalaman maksimum pohon
- learning_rate: Kecepatan pembelajaran
- subsample: Proporsi data yang digunakan untuk membangun setiap pohon
- Baseline model: Linear Regression (sebagai pembanding awal)
- Proses Improvement:
- GridSearchCV untuk melakukan hyperparameter tuning
- Cross-validation untuk menghindari overfitting

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Metrik yang digunakan:
- Mean Absolute Error (MAE): Rata-rata selisih absolut antara nilai aktual dan prediksi
- Root Mean Squared Error (RMSE): Akar dari rata-rata selisih kuadrat
- R² Score: Koefisien determinasi, seberapa baik model menjelaskan varians target

Hasil evaluasi:
XGBoost (tuned): MAE = 1.8, RMSE = 2.3, R² = 0.85

Dari hasil tersebut, XGBoost terbukti lebih unggul dibandingkan model baseline.
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

