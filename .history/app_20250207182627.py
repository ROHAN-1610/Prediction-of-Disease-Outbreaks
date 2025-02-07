import os
import pickle
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide", page_icon="🧑‍⚕️")

# Inject Custom CSS
st.markdown("""
    <style>
        .title {
            color: #4CAF50;
            font-size: 40px;
            text-align: center;
            font-weight: bold;
        }
        .subtitle {
            color: #555;
            font-size: 20px;
            text-align: center;
            font-style: italic;
        }
        .stTextInput {
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        }
        .custom-button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            display: block;
            margin: auto;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="title">Prediction of Disease Outbreaks</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">An AI-based health prediction system</p>', unsafe_allow_html=True)

# Load Models
working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/training_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/training_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/training_models/parkinsons_model.sav', 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"], 
                           menu_icon='hospital-fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)

# ==================== Diabetes Prediction Page ====================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    inputs = {
        "Pregnancies": st.text_input('Number of Pregnancies'),
        "Skin Thickness": st.text_input('Skin Thickness value'),
        "Diabetes Pedigree Function": st.text_input('Diabetes Pedigree Function value'),
        "Glucose": st.text_input('Glucose Level'),
        "Insulin": st.text_input('Insulin Level'),
        "Age": st.text_input('Age of the Person'),
        "Blood Pressure": st.text_input('Blood Pressure value'),
        "BMI": st.text_input('BMI value')
    }

    if st.button('Diabetes Test Result', key="diabetes_button"):
        user_input = [float(inputs[key]) for key in inputs]
        prediction = diabetes_model.predict([user_input])
        result = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
        st.success(result)

# ==================== Heart Disease Prediction Page ====================
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    inputs = {
        "Age": st.text_input('Age'),
        "Resting Blood Pressure": st.text_input('Resting Blood Pressure'),
        "Resting Electrocardiographic Results": st.text_input('Resting Electrocardiographic results'),
        "ST Depression": st.text_input('ST depression induced by exercise'),
        "Thal": st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect'),
        "Sex": st.text_input('Sex'),
        "Serum Cholesterol": st.text_input('Serum Cholesterol in mg/dl'),
        "Max Heart Rate": st.text_input('Maximum Heart Rate achieved'),
        "Slope": st.text_input('Slope of the peak exercise ST segment'),
        "Chest Pain Type": st.text_input('Chest Pain types'),
        "Fasting Blood Sugar": st.text_input('Fasting Blood Sugar > 120 mg/dl'),
        "Exercise Induced Angina": st.text_input('Exercise Induced Angina'),
        "Major Vessels": st.text_input('Major vessels colored by fluoroscopy')
    }

    if st.button('Heart Disease Test Result', key="heart_button"):
        user_input = [float(inputs[key]) for key in inputs]
        prediction = heart_disease_model.predict([user_input])
        result = 'The person has heart disease' if prediction[0] == 1 else 'The person does not have heart disease'
        st.success(result)

# ==================== Parkinson's Prediction Page ====================
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    inputs = {
        "MDVP:Fo(Hz)": st.text_input('MDVP:Fo(Hz)'),
        "MDVP:RAP": st.text_input('MDVP:RAP'),
        "Shimmer:APQ3": st.text_input('Shimmer:APQ3'),
        "HNR": st.text_input('HNR'),
        "D2": st.text_input('D2'),
        "MDVP:Fhi(Hz)": st.text_input('MDVP:Fhi(Hz)'),
        "MDVP:PPQ": st.text_input('MDVP:PPQ'),
        "Shimmer:APQ5": st.text_input('Shimmer:APQ5'),
        "RPDE": st.text_input('RPDE'),
        "PPE": st.text_input('PPE'),
        "MDVP:Flo(Hz)": st.text_input('MDVP:Flo(Hz)'),
        "Jitter:DDP": st.text_input('Jitter:DDP'),
        "MDVP:APQ": st.text_input('MDVP:APQ'),
        "DFA": st.text_input('DFA'),
        "MDVP:Jitter(%)": st.text_input('MDVP:Jitter(%)'),
        "MDVP:Shimmer": st.text_input('MDVP:Shimmer'),
        "Shimmer:DDA": st.text_input('Shimmer:DDA'),
        "Spread1": st.text_input('Spread1'),
        "MDVP:Jitter(Abs)": st.text_input('MDVP:Jitter(Abs)'),
        "MDVP:Shimmer(dB)": st.text_input('MDVP:Shimmer(dB)'),
        "NHR": st.text_input('NHR'),
        "Spread2": st.text_input('Spread2')
    }

    if st.button("Parkinson's Test Result", key="parkinsons_button"):
        user_input = [float(inputs[key]) for key in inputs]
        prediction = parkinsons_model.predict([user_input])
        result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(result)
