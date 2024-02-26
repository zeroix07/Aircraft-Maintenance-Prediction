# -*- coding: utf-8 -*-
"""Aircraft Maintenance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CLd9qxiN_R02cch14EfC_4P7SCy9Q9JN

**Aircraft Engine Predictive Maintenance Project**

**Overview**
Dalam proyek ini, kami bertujuan untuk mengembangkan model pemeliharaan prediktif untuk mesin pesawat. Tujuan utamanya adalah untuk memprediksi Sisa Umur Berguna (RUL) mesin ini berdasarkan pembacaan sensor dan parameter operasional. Pemeliharaan prediktif sangat penting untuk mengoptimalkan jadwal pemeliharaan, mengurangi waktu henti, dan memastikan pengoperasian pesawat yang efisien.

**Dataset**

Kumpulan data yang digunakan dalam proyek ini terdiri dari data sensor dan pengaturan mesin yang dikumpulkan dari waktu ke waktu. Ini mencakup fitur-fitur seperti pengaturan parameter, pengukuran sensor.

**Langkah-langkah:**

Proyek ini mengikuti langkah-langkah utama berikut:

**Data Preparation:** Menggabungkan set data pelatihan dan pengujian, menghitung RUL, dan menentukan kolom fitur.
Pemilihan Model: Memanfaatkan Regresi Linier sebagai model pilihan untuk memprediksi RUL.

**Training and Evaluation:** Melatih model pada set pelatihan dan mengevaluasi performanya menggunakan metrik seperti Mean Squared Error (MSE).

**Goals**

Mengembangkan model regresi untuk memprediksi secara akurat Sisa Umur Manfaat (RUL) mesin pesawat.
Memahami pentingnya berbagai fitur dalam menentukan kesehatan mesin.
Meletakkan dasar untuk eksplorasi di masa depan, yang berpotensi menggabungkan tugas klasifikasi untuk prediksi yang lebih bernuansa.
Mari selidiki detail setiap langkah dan jelajahi hasil model pemeliharaan prediktif kami.
"""

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report

#Load Dataset
df_train = pd.read_excel(r'/content/PM_train.xlsx')
df_test = pd.read_excel(r'/content/PM_test.xlsx')
df_truth = pd.read_excel(r'/content/PM_truth.xlsx')

"""**Data Concatenation**

Concat: Menggabungkan df_train dan df_test ke dalam satu kerangka data (df) agar berfungsi dengan seluruh kumpulan data.
"""

df = pd.concat([df_train, df_test], ignore_index=True)
df

df.columns

"""**Feature Engineering**

Remaining Useful Life (RUL) adalah konsep penting dalam pemeliharaan prediktif, yang mewakili perkiraan umur operasional atau siklus yang tersisa untuk suatu aset sebelum diperkirakan akan rusak. Dalam konteks mesin pesawat, RUL membantu mengantisipasi titik di mana mesin tidak lagi memenuhi persyaratan kinerja. Dengan menghitung RUL, organisasi dapat secara proaktif merencanakan aktivitas pemeliharaan, mengoptimalkan alokasi sumber daya, dan meminimalkan waktu henti. Pendekatan prediktif ini memungkinkan intervensi tepat waktu, mengurangi risiko kegagalan tak terduga dan meningkatkan efisiensi dan keandalan aset secara keseluruhan. RUL berfungsi sebagai metrik utama untuk membuat keputusan yang tepat dalam strategi pemeliharaan dan operasional.

- **Remaining Useful Life (RUL):** Dihitung dengan mengurangkan siklus saat ini dari siklus maksimum untuk setiap mesin.
- **Kolom Fitur**: Menentukan daftar kolom fitur untuk pelatihan model.
"""

df['RUL'] = df.groupby('id')['cycle'].transform(max) - df['cycle']
feature_columns = ['setting1', 'setting2', 'setting3', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21']

"""**Merging Data**

Merging: Menggabungkan df dengan df_truth berdasarkan ID mesin, memberikan informasi tambahan untuk analisis.
"""

df = pd.merge(df, df_truth, on='id', how='left')

"""**Labeling**

Threshold Labeling: Membuat label biner ('label') berdasarkan ambang batas 30 untuk RUL, yang membantu dalam menciptakan masalah klasifikasi.
"""

threshold = 30
df['label'] = (df['RUL'] <= threshold).astype(int)

"""**Train-Test Split**

Splitting Data: Menggunakan fungsi pemisahan train-test untuk membagi data menjadi set pelatihan dan pengujian. Model akan dilatih pada set pelatihan dan dievaluasi pada set pengujian.
"""

X_train, X_test, y_train, y_test = train_test_split(df[feature_columns], df['RUL'], test_size=0.2, random_state=42)

"""**Model Training**

Linear Regression Model: Membuat dan melatih model regresi linier menggunakan kolom fitur yang ditentukan sebelumnya.
"""

# Creating a linear regression model
model = LinearRegression()
# Train the model
model.fit(X_train, y_train)

"""**Prediction and Evaluation**

- Making Prediction : Menerapkan model terlatih untuk memprediksi RUL pada set pengujian.
- Binary Conversion: Mengubah nilai RUL menjadi label biner (0 atau 1) untuk evaluasi sebagai masalah klasifikasi.
- Evaluation Metrics: Menghitung metrik laporan akurasi dan klasifikasi untuk menilai kinerja model.
"""

# Make predictions on the test set
y_pred = model.predict(X_test)

# y_test contains the true labels and y_pred contains the predicted labels
y_test_binary = (y_test <= threshold).astype(int)
y_pred_binary = (y_pred <= threshold).astype(int)

# Evaluate the model
accuracy = accuracy_score(y_test_binary, y_pred_binary)
print(f'Accuracy: {accuracy}')
print(classification_report(y_test_binary, y_pred_binary))

"""**Conclusion**

Dalam proyek ini, kami bertujuan untuk memprediksi Sisa Umur Manfaat (RUL) mesin pesawat menggunakan pendekatan regresi. Kumpulan data, yang terdiri dari pembacaan sensor dan parameter mesin, digunakan untuk melatih model Regresi Linier. Langkah-langkah penting dalam proyek ini meliputi:

- Data Preprocessing: Menggabungkan kumpulan data pelatihan dan pengujian, menghitung RUL, dan menentukan kolom fitur.
- Model Training: Model Regresi Linier digunakan untuk memprediksi RUL berdasarkan fitur yang dipilih.
- Evaluation: Model dievaluasi menggunakan metrik seperti Mean Squared Error (MSE) dan akurasi untuk ambang batas tertentu.

Model Regresi Linier menunjukkan hasil yang menjanjikan dalam memprediksi RUL. Laporan akurasi dan klasifikasi menunjukkan efektivitasnya dalam memperkirakan sisa umur operasional mesin pesawat. Namun, penting untuk dicatat bahwa tidak ada tugas klasifikasi yang dilakukan dalam implementasi khusus ini.

Pekerjaan di masa depan mungkin melibatkan eksplorasi model klasifikasi untuk memprediksi hasil biner terkait kesehatan mesin, seperti apakah mesin akan gagal dalam jangka waktu tertentu. Hal ini akan memberikan pemahaman yang lebih mendalam mengenai kebutuhan pemeliharaan dan semakin meningkatkan penerapan praktis strategi pemeliharaan prediktif.
"""