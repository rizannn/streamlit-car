import pickle
import streamlit as st

# load save model 
model = pickle.load(open('caprice_model.sav', 'rb'))

# Judul Untuk Web
st.title('Data Mining Prediksi Car Popularity')


# Form Input
buying_price = st.text_input('Masukan Nilai Buying Price')

maintainence_cost = st.text_input('Masukan Nilai Maintainence Cost') 

number_of_doors = st.text_input('Masukan  Nilai Number Of Door')

number_of_seats = st.text_input('Masukan Nilai Number Of Seats')

luggage_boot_size = st.text_input('Masukan Nilai Luggage Boot Size')

safety_rating = st.text_input('Masukan Nilai Safety Rating')


# kode Prediksi
price_diagnosis = ' '

#Button Prediksi
if st.button('Test Popularity'):
    price_prediction = model.predict([[buying_price, maintainence_cost, number_of_doors, number_of_seats, luggage_boot_size, safety_rating]])

    if(price_prediction[0]==1):
       price_diagnosis = 'Popularity Sangat Rendah'

    elif(price_prediction[0]==2):
         price_diagnosis = 'Popularity Rendah'

    elif(price_prediction[0]==3):
         price_diagnosis = 'Popularity Sedang'

    else:
         price_diagnosis = 'Popularity Tinggi'

st.success(price_diagnosis)
