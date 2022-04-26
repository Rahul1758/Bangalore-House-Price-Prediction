import pickle
import json
import streamlit as st
from predict import Regressor


stacked_model = pickle.load(open('./Stacked_model.pkl', 'rb'))
loc = json.load(open('./locations.json', 'r'))['locations']
area_type_list = ['Super built-up Area', 'Built-up Area', 'Carpet Area', 'Plot Area']

def main():
    html_temp = """<div style="background-color:tomato;padding:10px">
                   <h2 style="color:white;text-align:center;">Bangalore House Price Predictor</h2>
                   </div>"""
    st.markdown(html_temp,unsafe_allow_html=True)
    location = st.selectbox('Enter locality of the house', loc)
    size = st.number_input('Enter the size of house in BHK', step=1, value=0)
    bath = st.number_input('Enter number of bathrooms in the house', step=1, value=0)
    total_sqft = st.number_input('Enter the area of house in sq.ft', value=0)
    area_type = st.selectbox('Enter type of area', area_type_list)
    
    if st.button('Predict'):
        regressor = Regressor()
        pred = regressor.get_predictions(area_type, location, size, total_sqft, bath, stacked_model)
        if pred>=100:
            st.write(f'#### The estimated price of this House is {round(pred/100, 2)} Crores')
        else:
            st.write(f'#### The estimated price of this House is {round(pred, 2)} lakhs')

if __name__=='__main__':
    main()