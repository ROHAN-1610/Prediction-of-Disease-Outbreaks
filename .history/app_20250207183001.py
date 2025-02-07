import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set Page Configuration
st.set_page_config(page_title="Disease Outbreak Prediction", layout="wide", page_icon="🧑‍⚕️")

# Inject Custom CSS
st.markdown("""
    <style>
        .title {
            color: #4CAF50;
            font-size: 36px;
            text-align: center;
            font-weight: bold;
        }
        .subtitle {
            color: #555;
            font-size: 18px;
            text-align: center;
            font-style: italic;
        }
        .stTextInput input {
            border: 2px solid #4CAF50 !important;
            border-radius: 5px !important;
            padding: 10px !important;
            font-size: 16px !important;
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

# Header
st.markdown('<h1 class="title">Disease Outbreak Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-powered prediction system for early diagnosis</p>', unsafe_allow_html=True)

# Load Models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/training_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/training_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/training_models/parkinsons_model.sav', 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"], 
                           menu_icon='hospital-fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)

# ========== Diabetes Prediction Page ==========
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')
    
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure')
        SkinThickness = st.text_input('Skin Thickness')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI Value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        Age = st.text_input('Age')

    if st.button('Get Diabetes Prediction', key="diabetes_button", help="Click to predict diabetes"):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            prediction = diabetes_model.predict([user_input])
            result = '✅ The person is diabetic' if prediction[0] == 1 else '❌ The person is not diabetic'
            st.success(result)
        except:
            st.error("⚠️ Please enter valid numerical values for all fields.")

# ========== Heart Disease Prediction Page ==========
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')
    
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.text_input('Age')
        Sex = st.text_input('Sex (0 = Female, 1 = Male)')
        ChestPainType = st.text_input('Chest Pain Type')
        BloodPressure = st.text_input('Resting Blood Pressure')
    
    with col2:
        Cholesterol = st.text_input('Serum Cholesterol (mg/dl)')
        FastingBloodSugar = st.text_input('Fasting Blood Sugar (> 120 mg/dl)')
        MaxHeartRate = st.text_input('Maximum Heart Rate Achieved')
        ExerciseInducedAngina = st.text_input('Exercise Induced Angina')

    if st.button('Get Heart Disease Prediction', key="heart_button", help="Click to predict heart disease"):
        try:
            user_input = [float(Age), float(Sex), float(ChestPainType), float(BloodPressure), 
                          float(Cholesterol), float(FastingBloodSugar), float(MaxHeartRate), float(ExerciseInducedAngina)]
            prediction = heart_disease_model.predict([user_input])
            result = '✅ The person has heart disease' if prediction[0] == 1 else '❌ The person does not have heart disease'
            st.success(result)
        except:
            st.error("⚠️ Please enter valid numerical values for all fields.")

# ========== Parkinson's Prediction Page ==========
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        Fo = st.text_input('MDVP:Fo(Hz)')
        RAP = st.text_input('MDVP:RAP')
        APQ3 = st.text_input('Shimmer:APQ3')
        HNR = st.text_input('HNR')
    
    with col2:
        D2 = st.text_input('D2')
        PPQ = st.text_input('MDVP:PPQ')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')

    if st.button("Get Parkinson's Prediction", key="parkinsons_button", help="Click to predict Parkinson's"):
        try:
            user_input = [float(Fo), float(RAP), float(APQ3), float(HNR), float(D2), float(PPQ), float(RPDE), float(PPE)]
            prediction = parkinsons_model.predict([user_input])
            result = "✅ The person has Parkinson's disease" if prediction[0] == 1 else "❌ The person does not have Parkinson's disease"
            st.success(result)
        except:
            st.error("⚠️ Please enter valid numerical values for all fields.")
