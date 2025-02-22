import streamlit as st
from datetime import datetime

# Title and description
st.title("Age Converter Application")
st.write("This application helps you calculate your age based on your date of birth.")

# Style the background and layout
st.markdown("""
    <style>
        .stApp {
            background-color: #F0F8FF;
        }
        .stTextInput>label {
            font-size: 20px;
        }
        .stButton>button {
            font-size: 18px;
            background-color: #008CBA;
            color: white;
        }
        .stText {
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Input for date of birth
dob = st.date_input("Select your Date of Birth", min_value=datetime(1900, 1, 1))

# Button to calculate the age
if st.button('Calculate Age'):
    # Current date
    today = datetime.today()
    
    # Age calculation
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    # Display the result
    st.write(f"Your age is: {age} years old.")

