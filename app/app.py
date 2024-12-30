# Description: This is the main file for the Streamlit app.
#              It will be used to load the model and make predictions.
#path: ./app/app.py
# libraries
import streamlit as st
import pandas as pd
import joblib

from utils import get_options, translate_pred

# modelo
pipeline = joblib.load('./app/model/stacking_optimized_0.pkl')

#título
st.title('Income Prediction App')
st.write("Fill out the form to get your income prediction: it's free!")
st.write('The income prediction is based on the US Census data. Please provide ALL the information requested below:')
#inputs
options = get_options()
age            = st.number_input('Age',min_value= 15, max_value= 150,
                                 value= 20, step= 1)
hours_per_week = st.number_input('Working hs per week', min_value= 0,
                                 max_value= 90, value= 40, step= 1)

capital_gain   = st.number_input('Capital Gain', min_value= 0, step= 100)
capital_loss   = st.number_input('Capital Loss', min_value= 0, step= 100)

marital_status = st.selectbox('Marital Status', options= options['marital_opt'] )
relationship   = st.selectbox('Relationship',   options= options['relationship_opt'])
education      = st.selectbox('Education',      options= options['education_opt'])
occupation     = st.selectbox('Occupation',     options= options['occupation_opt'])

capital_net    = capital_gain - capital_loss

if st.button('Predict'):
    new_data = pd.DataFrame({'age': [age],
                             'hours_per_week': [hours_per_week],
                             'marital_status': [marital_status],
                             'relationship'  : [relationship],
                             'education'     : [education],
                             'occupation'    : [occupation],
                             'capital_net'   : [capital_net]})
    
    pred_class, prob_no, prob_yes = translate_pred(pipeline, new_data, return_prob= True)
    if pred_class == 'no':
        prediction = 'have an anual income LESS OR EQUAL to 50K :('
    else:
        prediction = 'have an anual income GREATER than 50K. Thats fancy. Buy me things! :D'
    st.write(f'Prediction:\nGiven the info you provided, the model predicts that you {prediction}')
    st.write('Probability of having an income:\n')
    st.write(f'- LESS OR EQUAL to 50K: {prob_no:.2f}')
    st.write(f'- GREATER than 50K:     {prob_yes:.2f}')
 


