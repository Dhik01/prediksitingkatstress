import pickle
import streamlit as st

model = pickle.load(open('PrediksiTingkatStress.sav','rb'))

st.title('Prediksi Tingkat Stress Seseorang')

Humidity = st.number_input('Masukkan Nilai Kelembapan Ruangan Yang Sering Ditempati Pasien (%RH): ')
Temperature = st.number_input('Masukkan Nilai Suhu Ruangan Yang Sering Ditempati Pasien (F/Fahrenheit): ')
Step_count = st.number_input('Masukkan Jumlah Aktivitas Yang Dilakukan Pasien Tiap Harinya : ')

predict = ''
if st.button('Hasil Prediksi'):
    predict = model.predict([[Humidity, Temperature, Step_count]])

    if(predict[0] == 0):
        predict = 'Pasien Mengalami Stress Rendah'
    elif predict[0]==1:
        predict = 'Pasien Mengalami Stress Sedang'
    else:
        predict = 'Pasien Mengalami Stress Tinggi'
st.success(predict)