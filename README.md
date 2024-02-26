# Laporan Proyek Machine Learning - Fadhel Muhammad Apriansyah

## Domain Proyek

Dalam industri penerbangan, pemeliharaan pesawat adalah bagian penting dalam memastikan keamanan dan kinerja pesawat. Namun, pemeliharaan yang tidak terjadwal atau terlalu sering dapat menyebabkan gangguan operasional dan biaya yang tinggi. Di sisi lain, kurangnya pemeliharaan yang memadai dapat meningkatkan risiko kegagalan dan bahaya keselamatan.

Dalam upaya untuk meningkatkan efisiensi dan efektivitas pemeliharaan pesawat, banyak perusahaan penerbangan mulai mengadopsi pendekatan yang didorong oleh data. Dengan menggunakan teknik-teknik pemeliharaan berbasis prediksi, perusahaan dapat merencanakan pemeliharaan secara lebih cerdas, mengoptimalkan penggunaan sumber daya, dan mengurangi gangguan yang tidak terduga dalam operasi penerbangan.

Salah satu pendekatan yang digunakan adalah menggunakan teknik machine learning, seperti regresi linear, untuk memprediksi kebutuhan pemeliharaan pesawat. Dengan menganalisis data historis tentang pemeliharaan, pengoperasian pesawat, dan faktor-faktor lain yang mempengaruhi kondisi pesawat, model regresi linear dapat digunakan untuk memperkirakan waktu pemeliharaan berikutnya, mendeteksi potensi kegagalan komponen, atau bahkan memprediksi sumber daya yang diperlukan untuk pemeliharaan di masa mendatang.

Dengan demikian, penggunaan regresi linear dalam proyek pemeliharaan pesawat menjadi salah satu langkah yang menarik dalam upaya untuk meningkatkan efisiensi, keselamatan, dan kinerja operasional dalam industri penerbangan.


## Business Understanding

### Problem Statements

1. **Pernyataan Masalah 1**: Saat ini, perusahaan kami mengalami tantangan dalam mengoptimalkan jadwal pemeliharaan pesawat. Pemeliharaan yang tidak terjadwal sering kali membutuhkan waktu dan biaya yang tidak terduga, sementara terlalu sedikit pemeliharaan dapat meningkatkan risiko kegagalan dan menurunkan keandalan pesawat.

2. **Pernyataan Masalah 2**: Kurangnya visibilitas terhadap kondisi aktual pesawat seringkali membuat perencanaan pemeliharaan menjadi kurang efisien. Informasi yang tidak lengkap atau terlambat dapat mengakibatkan penundaan dalam pemeliharaan yang mengganggu jadwal operasional dan meningkatkan biaya.

### Goals

1. **Jawaban Pernyataan Masalah 1**: Mengembangkan model prediksi menggunakan regresi linear untuk memperkirakan waktu pemeliharaan berikutnya berdasarkan faktor-faktor seperti jumlah jam terbang, usia pesawat, dan kondisi komponen. Tujuannya adalah untuk mengurangi pemeliharaan yang tidak terjadwal dan meningkatkan efisiensi operasional.

2. **Jawaban Pernyataan Masalah 2**: Membuat sistem pemantauan real-time yang dapat mengumpulkan dan menganalisis data pesawat secara terus-menerus. Dengan demikian, tujuannya adalah untuk meningkatkan visibilitas terhadap kondisi pesawat dan memungkinkan perencanaan pemeliharaan yang lebih tepat waktu dan efisien.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.


## Data Understanding
[Sumber Dataset : Kaggle](https://www.kaggle.com/datasets/aadharshviswanath/aircraft-sensor-and-engine-performance/data)


### Variabel-variabel:
- id: Pengidentifikasi unik untuk setiap entri data.
- cycle: Menunjukkan siklus atau periode operasional, yang menunjukkan tahapan atau durasi pengoperasian mesin.
- setting1, setting2, setting3: Nilai numerik yang mewakili berbagai pengaturan operasional atau parameter mesin pesawat.
- s1 hingga s21: Pembacaan sensor numerik diperoleh dari 21 sensor berbeda yang dipasang pada mesin. Pembacaan ini mencakup berbagai pengukuran fisik, termasuk namun tidak terbatas pada suhu, tekanan, dan parameter relevan lainnya.

Kumpulan data "kebenaran" yang menyertainya mengaitkan setiap catatan dengan variabel tambahan, yang mungkin berfungsi sebagai target atau label. Kolom "id" dalam kumpulan data "truth" kemungkinan besar sesuai dengan masing-masing pengidentifikasi dalam kumpulan data utama, sehingga membangun hubungan antara pembacaan sensor dan nilai kebenaran yang diberikan.

## Data Preparation
Data Concatenation, Feature Engineering, Merging Data, Labeling, splitting dataset


## Modeling
Linear Regression Model

## Evaluation
Making Prediction : Menerapkan model terlatih untuk memprediksi RUL pada set pengujian.
Binary Conversion: Mengubah nilai RUL menjadi label biner (0 atau 1) untuk evaluasi sebagai masalah klasifikasi.
Evaluation Metrics: Menghitung metrik laporan akurasi dan klasifikasi untuk menilai kinerja model.
