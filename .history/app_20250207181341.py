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
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'], 
                           menu_icon='hospital-fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)

# ==================== Diabetes Prediction Page ====================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ""

    if st.button('Diabetes Test Result', key="diabetes_button"):
        user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict([user_input])

        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

    st.success(diab_diagnosis)

    # Custom JavaScript Alert Button
    components.html("""
    <script>
        function showAlert() {
            alert('Diabetes Test Button Clicked!');
        }
    </script>
    <button class="custom-button" onclick="showAlert()">Show Alert</button>
    """, height=50)

# ==================== Heart Disease Prediction Page ====================
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ""

    if st.button('Heart Disease Test Result', key="heart_button"):
        user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        heart_prediction = heart_disease_model.predict([user_input])

        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'

    st.success(heart_diagnosis)

# ==================== Parkinson's Prediction Page ====================
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    # Add more fields similarly...

    parkinsons_diagnosis = ""

    if st.button("Parkinson's Test Result", key="parkinsons_button"):
        user_input = [float(x) for x in [fo, fhi, flo, Jitter_percent, Jitter_Abs]]  # Add all necessary fields here
        parkinsons_prediction = parkinsons_model.predict([user_input])

        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
