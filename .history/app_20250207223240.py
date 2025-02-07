import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide", page_icon="🧑‍⚕️")

st.markdown("""
    <style>
    /* General App Styling - Smooth Background */
    .stApp {
        background: linear-gradient(135deg, #E3F2FD, #F1E7FE, #D7E1EC);
        font-family: 'Poppins', sans-serif;
        color: #2C3E50;
    }
    
    /* Sidebar - Deep Elegant Gradient */
    .stSidebar {
        background: linear-gradient(135deg, #3A0CA3, #7209B7, #4361EE);
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(114, 9, 183, 0.5);
        position: relative;
    }
    .stSidebar h1, .stSidebar h2, .stSidebar h3 {
        color: white;
        text-shadow: 0px 0px 8px rgba(255,255,255,0.5);
    }

    /* 🛠 Fix Sidebar Collapse Arrow */
    [data-testid="collapsedControl"] {
        color: white !important; /* Ensure it's visible */
        font-size: 22px !important;
        opacity: 1 !important;
        z-index: 100;
    }
    [data-testid="collapsedControl"]:hover {
        color: #FFEB3B !important; /* Bright yellow on hover */
        transform: scale(1.2);
        transition: all 0.3s ease-in-out;
    }

    /* Button Styling - Soft Glow Effect */
    .stButton>button {
        background: linear-gradient(135deg, #3A0CA3, #7209B7, #4361EE);
        color: white !important;
        border-radius: 12px;
        padding: 14px 28px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 10px rgba(114, 9, 183, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4361EE, #7209B7, #3A0CA3);
        transform: scale(1.08);
        box-shadow: 0px 8px 16px rgba(114, 9, 183, 0.6);
        border: 2px solid white;
    }

    /* Text Input Fields - Glass Effect */
    .stTextInput>div>div>input {
        border-radius: 12px;
        padding: 14px;
        border: 2px solid rgba(67, 97, 238, 0.8);
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        color: white;
        transition: all 0.3s ease-in-out;
    }
    .stTextInput>div>div>input:focus {
        border: 2px solid #7209B7;
        box-shadow: 0px 4px 8px rgba(114, 9, 183, 0.6);
    }

    /* Titles and Headings - Gradient Text */
    .stTitle, .stHeader, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: transparent;
        background: linear-gradient(90deg, #3A0CA3, #7209B7);
        background-clip: text;
        -webkit-background-clip: text;
        font-weight: bold;
        text-align: center;
        text-shadow: 0px 0px 8px rgba(114, 9, 183, 0.3);
    }

    /* Custom Cards - Glassmorphism */
    .stContainer {
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(12px);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stContainer:hover {
        transform: translateY(-6px);
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)





# Getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/training_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/training_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/training_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Diabetes Prediction Page
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

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
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
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
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

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
