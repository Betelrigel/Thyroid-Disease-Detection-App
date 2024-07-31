import streamlit as st
import pandas as pd
import joblib
import os

# Load the pre-trained model
if os.path.exists('model.pkl'):
    model = joblib.load('model.pkl')
    st.success("Model loaded successfully.")
else:
    st.error("Model file not found. Please run train_model.py first.")
    model = None

# Create a function to make predictions
def predict_thyroid(features):
    if model is None:
        st.error("Model is not loaded.")
        return None
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app
st.title("Thyroid Disease Prediction")
st.markdown("""
<style>
    .title-style {
        font-size:24px;
        font-weight:bold;
        color:#004080;
    }
    .header-style {
        font-size:20px;
        font-weight:bold;
        color:#004080;
    }
    .normal-text {
        font-size:16px;
        font-weight:normal;
        color:#004080;
    }
    .highlight-text {
        font-size:16px;
        font-weight:bold;
        color:#000000; /* Black for better readability */
    }
    .table-style {
        border-collapse: collapse;
        width: 100%;
        margin-top: 20px;
    }
    .table-style th, .table-style td {
        border: 1px solid #004080;
        padding: 10px;
        text-align: left;
        vertical-align: top;
    }
    .table-style th {
        background-color: #004080;
        color: white;
    }
    .table-style tr:nth-child(even) {
        background-color: #f2f2f2;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.header('Patient Data')

# Define user input fields
def user_input_features():
    age = st.sidebar.slider('Age', 1, 100, 50)
    sex = st.sidebar.selectbox('Sex', ('Male', 'Female'))
    on_thyroxine = st.sidebar.selectbox('On Thyroxine', ('Yes', 'No'))
    query_on_thyroxine = st.sidebar.selectbox('Query On Thyroxine', ('Yes', 'No'))
    on_antithyroid_medication = st.sidebar.selectbox('On Antithyroid Medication', ('Yes', 'No'))
    sick = st.sidebar.selectbox('Sick', ('Yes', 'No'))
    pregnant = st.sidebar.selectbox('Pregnant', ('Yes', 'No'))
    thyroid_surgery = st.sidebar.selectbox('Thyroid Surgery', ('Yes', 'No'))
    I131_treatment = st.sidebar.selectbox('I131 Treatment', ('Yes', 'No'))
    query_hypothyroid = st.sidebar.selectbox('Query Hypothyroid', ('Yes', 'No'))
    query_hyperthyroid = st.sidebar.selectbox('Query Hyperthyroid', ('Yes', 'No'))
    lithium = st.sidebar.selectbox('Lithium', ('Yes', 'No'))
    goitre = st.sidebar.selectbox('Goitre', ('Yes', 'No'))
    tumor = st.sidebar.selectbox('Tumor', ('Yes', 'No'))
    hypopituitary = st.sidebar.selectbox('Hypopituitary', ('Yes', 'No'))
    psych = st.sidebar.selectbox('Psych', ('Yes', 'No'))
    TSH = st.sidebar.number_input('TSH', value=0.0)
    T3 = st.sidebar.number_input('T3', value=0.0)
    TT4 = st.sidebar.number_input('TT4', value=0.0)
    T4U = st.sidebar.number_input('T4U', value=0.0)
    FTI = st.sidebar.number_input('FTI', value=0.0)

    sex = 1 if sex == 'Male' else 0
    on_thyroxine = 1 if on_thyroxine == 'Yes' else 0
    query_on_thyroxine = 1 if query_on_thyroxine == 'Yes' else 0
    on_antithyroid_medication = 1 if on_antithyroid_medication == 'Yes' else 0
    sick = 1 if sick == 'Yes' else 0
    pregnant = 1 if pregnant == 'Yes' else 0
    thyroid_surgery = 1 if thyroid_surgery == 'Yes' else 0
    I131_treatment = 1 if I131_treatment == 'Yes' else 0
    query_hypothyroid = 1 if query_hypothyroid == 'Yes' else 0
    query_hyperthyroid = 1 if query_hyperthyroid == 'Yes' else 0
    lithium = 1 if lithium == 'Yes' else 0
    goitre = 1 if goitre == 'Yes' else 0
    tumor = 1 if tumor == 'Yes' else 0
    hypopituitary = 1 if hypopituitary == 'Yes' else 0
    psych = 1 if psych == 'Yes' else 0

    data = {
        'age': age,
        'sex': sex,
        'on thyroxine': on_thyroxine,
        'query on thyroxine': query_on_thyroxine,
        'on antithyroid medication': on_antithyroid_medication,
        'sick': sick,
        'pregnant': pregnant,
        'thyroid surgery': thyroid_surgery,
        'I131 treatment': I131_treatment,
        'query hypothyroid': query_hypothyroid,
        'query hyperthyroid': query_hyperthyroid,
        'lithium': lithium,
        'goitre': goitre,
        'tumor': tumor,
        'hypopituitary': hypopituitary,
        'psych': psych,
        'TSH': TSH,
        'T3': T3,
        'TT4': TT4,
        'T4U': T4U,
        'FTI': FTI,
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display the user inputs
st.subheader('User Input Features')
st.write(input_df)

# Add a section for normal levels and implications of abnormal levels
st.subheader('Thyroid Test Information')

# Define normal levels and implications
normal_levels = {
    "TSH": "0.5 - 5.0 mIU/L",
    "Free T4 (Thyroxine)": "0.7 - 1.9 ng/dL",
    "Total T4": "5.0 - 12.0 µg/dL",
    "Total T3": "80 - 220 ng/dL"
}
implications = {
    "High TSH": "Possible hypothyroidism.",
    "Low TSH": "Possible hyperthyroidism.",
    "Low Free T4": "Possible hypothyroidism.",
    "High Free T4": "Possible hyperthyroidism.",
    "Low Total T4": "Possible hypothyroidism",
    "High Total T4": "Possible hyperthyroidism",
    "High Total T3": "Possible hyperthyroidism."
}

# Create a DataFrame for display
thyroid_info = pd.DataFrame({
    "Thyroid Test": ["TSH", "Free T4 (Thyroxine)", "Total T4", "Total T3"],
    "Normal Range": [normal_levels["TSH"], normal_levels["Free T4 (Thyroxine)"], normal_levels["Total T4"], normal_levels["Total T3"]],
    "Implications of Abnormal Levels": [
        f"High TSH: <span class='highlight-text'>{implications['High TSH']}</span><br>Low TSH: <span class='highlight-text'>{implications['Low TSH']}</span>",
        f"Low Free T4: <span class='highlight-text'>{implications['Low Free T4']}</span><br>High Free T4: <span class='highlight-text'>{implications['High Free T4']}</span>",
        f"Low Total T4: <span class='highlight-text'>{implications['Low Total T4']}</span><br>High Total T4: <span class='highlight-text'>{implications['High Total T4']}</span>",
        f"High Total T3: <span class='highlight-text'>{implications['High Total T3']}</span>"
    ]
})

# Display table with custom styling
st.markdown("""
<div class="table-style">
    <table>
        <thead>
            <tr>
                <th style="width: 33%;">Thyroid Test</th>
                <th style="width: 33%;">Normal Range</th>
                <th style="width: 33%;">Implications of Abnormal Levels</th>
            </tr>
        </thead>
        <tbody>
""", unsafe_allow_html=True)

for index, row in thyroid_info.iterrows():
    st.markdown(f"""
        <tr>
            <td style="width: 33%;">{row['Thyroid Test']}</td>
            <td style="width: 33%;">{row['Normal Range']}</td>
            <td style="width: 33%;">{row['Implications of Abnormal Levels']}</td>
        </tr>
    """, unsafe_allow_html=True)

st.markdown("</tbody></table></div>", unsafe_allow_html=True)

# Make a prediction and display the result
if st.button('Predict'):
    prediction = predict_thyroid(input_df.values[0])
    if prediction is not None:
        if prediction == 1:
            st.subheader('Prediction: Positive for Thyroid Disease')
        else:
            st.subheader('Prediction: Negative for Thyroid Disease')

st.markdown("""
<div class="normal-text">
    Note: Please consult with a healthcare professional for accurate diagnosis and treatment.
</div>
""", unsafe_allow_html=True)
