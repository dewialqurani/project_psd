import streamlit as st

import pandas as pd
import numpy as np

import pickle

from sklearn import metrics

st.set_page_config(
    page_title="Projectkk"
)

tab1, tab2 = st.tabs(["Dataset", "Implementation"])

with tab1:
    st.title('Klasifikasi Kelayakan Calon Pendonor Darah Menggunakan Metode Naive Bayes')
    st.write('Studi Kasus PMI Kabupaten Bangkalan')
    st.write('Darah adalah cairan yang terdapat pada semua makhluk hidup (kecuali tumbuhan) tingkat tinggi yang berfungsi mengirimkan zat – zat dan oksigen yang dibutuhkan oleh jaringan tubuh, mengangkut bahan – bahan kimia hasil metabolisme dan juga sebagai pertahanan tubuh terhadap virus atau bakteri [1] (Desmawati, 2013). ')
    
    st.write('Dalam tubuh orang dewasa, kira – kira 4 sampai 5 liter darah yang beredar terus - menerus melalui jaringan yang rumit mulai dari pembuluh darah, didorong oleh kontraksi kuat dari detak jantung. Setelah darah bergerak menjauh dari paru – paru dan jantung, melewati arteri besar dan mengalir ke jaringan yang sempit dan lebih kompleks dari pembuluh – pembuluh kecil, darah berinteraksi dengan sel – sel individual dari jaringan. Pada tingkat ini, fungsi utamanya adalah untuk memberi makan sel – sel tersebut, memberi mereka nutrisi, termasuk oksigen yang merupakan unsur paling dasar yang diperlukan untuk keberlangsungan hidup manusia. Dalam pertukaran nutrisi bermanfaat ini, darah menggambil dan membawa pergi limbah seluler seperti karbon dioksida yang pada akhirnya akan dikeluarkan dari tubuh ketika darah mengalir kembali ke paru – paru. ')
    st.markdown("""
    Link Dataset
    <a href="https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci"> Klik Disini</a>
    """, unsafe_allow_html=True)


    df = pd.read_csv("heart.csv")
    st.write("Dataset Penyakit Jantung : ")
    st.write(df)
    st.write("Note Nama - Nama Kolom : ")

    st.write("""
    <ol>
    <li>Age : Umur dalam satuan Tahun</li>
    <li>Sex : Jenis Kelamin (1=Laki-laki, 0=Perempuan)</li>
    <li>Cp : chest pain type (tipe sakit dada)(0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic)</li>
    <li>Trestbps : tekanan darah saat dalam kondisi istirahat dalam mm/Hg</li>
    <li>Chol : serum sholestoral (kolestrol dalam darah) dalam Mg/dl </li>
    <li>Fbs : fasting blood sugar (kadar gula dalam darah setelah berpuasa) lebih dari 120 mg/dl (1=Iya, 0=Tidak)</li>
    <li>Restecg : hasil test electrocardiographic (0 = normal, 1 = memiliki kelainan gelombang ST-T (gelombang T inversi dan/atau ST elevasi atau depresi > 0,05 mV), 2 = menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri dengan kriteria Estes)</li>
    <li>Thalach : rata-rata detak jantung pasien dalam satu menit</li>
    <li>Exang :  keadaan dimana pasien akan mengalami nyeri dada apabila berolah raga, 0 jika tidak nyeri, dan 1 jika menyebabkan nyeri</li>
    <li>Oldpeak : depresi ST yang diakibatkan oleh latihan relative terhadap saat istirahat</li>
    <li>Slope : slope dari puncak ST setelah berolah raga. Atribut ini memiliki 3 nilai yaitu 0 untuk downsloping, 1 untuk flat, dan 2 untuk upsloping.</li>
    <li>Ca: banyaknya pembuluh darah yang terdeteksi melalui proses pewarnaan flourosopy</li>
    <li>Thal: detak jantung pasien. Atribut ini memiliki 3 nilai yaitu 1 untuk fixed defect, 2 untuk normal dan 3 untuk reversal defect</li>
    <li>Target: hasil diagnosa penyakit jantung, 0 untuk terdiagnosa positif terkena penyakit jantung koroner, dan 1 untuk negatif terkena penyakit jantung koroner.</li>
    </ol>
    """,unsafe_allow_html=True)
