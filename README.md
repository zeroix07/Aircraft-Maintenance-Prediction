# Laporan Proyek Machine Learning - Fadhel Muhammad Apriansyah

## Domain Proyek

Dalam industri penerbangan, pemeliharaan pesawat adalah bagian penting dalam memastikan keamanan dan kinerja pesawat. Namun, pemeliharaan yang tidak terjadwal atau terlalu sering dapat menyebabkan gangguan operasional dan biaya yang tinggi. Di sisi lain, kurangnya pemeliharaan yang memadai dapat meningkatkan risiko kegagalan dan bahaya keselamatan.

Dalam upaya untuk meningkatkan efisiensi dan efektivitas pemeliharaan pesawat, banyak perusahaan penerbangan mulai mengadopsi pendekatan yang didorong oleh data. Dengan menggunakan teknik-teknik pemeliharaan berbasis prediksi, perusahaan dapat merencanakan pemeliharaan secara lebih cerdas, mengoptimalkan penggunaan sumber daya, dan mengurangi gangguan yang tidak terduga dalam operasi penerbangan.

Salah satu pendekatan yang digunakan adalah menggunakan teknik machine learning, seperti regresi linear, untuk memprediksi kebutuhan pemeliharaan pesawat. Dengan menganalisis data historis tentang pemeliharaan, pengoperasian pesawat, dan faktor-faktor lain yang mempengaruhi kondisi pesawat, model regresi linear dapat digunakan untuk memperkirakan waktu pemeliharaan berikutnya, mendeteksi potensi kegagalan komponen, atau bahkan memprediksi sumber daya yang diperlukan untuk pemeliharaan di masa mendatang. Dengan demikian, penggunaan regresi linear dalam proyek pemeliharaan pesawat menjadi salah satu langkah yang menarik dalam upaya untuk meningkatkan efisiensi, keselamatan, dan kinerja operasional dalam industri penerbangan.

Latar belakang yang membuat saya memilih project ini yaitu:
- Pemeliharaan pesawat yang efisien adalah kunci dalam industri penerbangan untuk menjaga keamanan dan mengurangi biaya operasional.
- Siklus operasional dan pengaturan mesin berpotensi memengaruhi kebutuhan pemeliharaan, namun, pengaruhnya mungkin kompleks dan sulit diprediksi.
- Data sensor yang tersedia dari mesin pesawat, seperti pembacaan suhu, tekanan, dan parameter lainnya, memberikan informasi yang berharga untuk memahami kondisi mesin dan meramalkan pemeliharaan yang diperlukan.

Lalu bagaimana memprediksi waktu pemeliharaan pesawat berikutnya berdasarkan siklus operasional dan parameter mesin?

## Business Understanding

### Problem Statements

1. **Bagaimana kita dapat memprediksi waktu pemeliharaan berikutnya untuk pesawat berdasarkan siklus operasional dan pengaturan mesin?**

2. **Apakah ada cara untuk meningkatkan efisiensi perencanaan pemeliharaan pesawat dengan memanfaatkan data sensor yang tersedia?**

### Goals

1. Mengembangkan model prediksi menggunakan regresi linear untuk memperkirakan waktu pemeliharaan berikutnya berdasarkan siklus operasional dan parameter mesin.

2. Jawaban Pernyataan Masalah 2: Membangun sistem analisis data yang dapat menggunakan pembacaan sensor dari mesin pesawat untuk meningkatkan visibilitas kondisi pesawat dan merencanakan pemeliharaan yang lebih efisien.


## Data Understanding
- Deskripsi Dataset
  Dataset ini berisi informasi tentang pemeliharaan pesawat, termasuk siklus operasional, pengaturan mesin, dan pembacaan sensor dari mesin pesawat. Data ini dikumpulkan dari serangkaian penerbangan dan pemeliharaan pada armada pesawat
  [Sumber Dataset : Kaggle](https://www.kaggle.com/datasets/aadharshviswanath/aircraft-sensor-and-engine-performance/data)

- Jumlah Data: 32569 entri

### Variabel-variabel:
- id: Pengidentifikasi unik untuk setiap entri data.
- cycle: Menunjukkan siklus atau periode operasional, yang menunjukkan tahapan atau durasi pengoperasian mesin.
- setting1, setting2, setting3: Nilai numerik yang mewakili berbagai pengaturan operasional atau parameter mesin pesawat.
- s1 hingga s21: Pembacaan sensor numerik diperoleh dari 21 sensor berbeda yang dipasang pada mesin. Pembacaan ini mencakup berbagai pengukuran fisik, termasuk namun tidak terbatas pada suhu, tekanan, dan parameter relevan lainnya.

Kumpulan data "kebenaran" yang menyertainya mengaitkan setiap catatan dengan variabel tambahan, yang mungkin berfungsi sebagai target atau label. Kolom "id" dalam kumpulan data "truth" kemungkinan besar sesuai dengan masing-masing pengidentifikasi dalam kumpulan data utama, sehingga membangun hubungan antara pembacaan sensor dan nilai kebenaran yang diberikan.

## Data Preparation
- Data Concatenation
  Concat: Menggabungkan df_train dan df_test ke dalam satu kerangka data (df) agar berfungsi dengan seluruh kumpulan data.
- Feature Engineering
  Remaining Useful Life (RUL) adalah konsep penting dalam pemeliharaan prediktif, yang mewakili perkiraan umur operasional atau siklus yang tersisa untuk suatu aset sebelum diperkirakan akan rusak. Dalam konteks mesin pesawat, RUL
  membantu mengantisipasi titik di mana mesin tidak lagi memenuhi persyaratan kinerja. Dengan menghitung RUL, organisasi dapat secara proaktif merencanakan aktivitas pemeliharaan, mengoptimalkan alokasi sumber daya, dan meminimalkan
  waktu henti. Pendekatan prediktif ini memungkinkan intervensi tepat waktu, mengurangi risiko kegagalan tak terduga dan meningkatkan efisiensi dan keandalan aset secara keseluruhan. RUL berfungsi sebagai metrik utama untuk membuat
  keputusan yang tepat dalam strategi pemeliharaan dan operasional.
- Merging Data
  Merging: Menggabungkan df dengan df_truth berdasarkan ID mesin, memberikan informasi tambahan untuk analisis.
- Labeling
  Threshold Labeling: Membuat label biner ('label') berdasarkan ambang batas 30 untuk RUL, yang membantu dalam menciptakan masalah klasifikasi.
- Train-Test Split
  Splitting Data: Menggunakan fungsi pemisahan train-test untuk membagi data menjadi set pelatihan dan pengujian. Model akan dilatih pada set pelatihan dan dievaluasi pada set pengujian.

## Modeling
1. Pemilihan Model
   Model yang dipilih untuk proyek ini adalah Linear Regression, karena kita mencoba memprediksi variabel kontinu (waktu pemeliharaan berikutnya) berdasarkan variabel-variabel prediktor.
2. Persiapan Data
   Data yang telah dipersiapkan sebelumnya dalam tahap Data Preparation digunakan sebagai input untuk model linear regression.
3. Inisialisasi Model
   Model linear regression diinisialisasi menggunakan fungsi LinearRegression() dari library scikit-learn.
4. Pelatihan Model
   Model linear regression dilatih menggunakan data pelatihan (training set) yang telah dibagi sebelumnya. Proses pelatihan ini melibatkan penyesuaian koefisien model untuk menghasilkan garis regresi yang terbaik sesuai dengan data.

## Evaluation

F1 score dan accuracy biasanya digunakan untuk evaluasi pada tugas klasifikasi, sedangkan dalam kasus regresi seperti yang Anda jelaskan (untuk memprediksi waktu pemeliharaan pesawat), metrik evaluasi yang lebih umum digunakan adalah Mean Squared Error (MSE), Root Mean Squared Error (RMSE), dan koefisien determinasi (R-squared). Model ini telah berhasil memperoleh akurasi sebesar 94%

![image](https://github.com/zeroix07/Aircraft-Maintenance-Prediction/assets/120600614/338c3051-6623-4ce8-b4d5-03b63508f2c9)
