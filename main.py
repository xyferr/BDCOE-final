import streamlit as st
import requests
import time

# background image ke liye embedded css
background_image = r"C:\ROHIT\CS\ML\projects\BDCOE-final\data\ele.jpg"
background_css = """
    <style>
        .stApp {
            background-image: url("https://www.teahub.io/photos/full/215-2159797_elephants-in-sundown.jpg");
            background-size: cover;    
        }
    </style>
"""

# title ko box me likhne ke liye embedded css
st.markdown(background_css, unsafe_allow_html=True)
st.markdown("""
    <div style="background-color:#ede6e8; padding:5px; border-radius:5px;">
        <h1 style="color:black; text-align:center;">⛔ Endangered  Animals🫏 Detection</h1>
    </div>
""", unsafe_allow_html=True)
#st.title(":blue[⛔Endangered Animals🫏 Detection]")

uploaded_file = st.file_uploader("Choose a wildlife image...", type=["jpg", "jpeg", "png", "webp", "avif"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    #  FastAPI backend ko image send karna post request ke dwara
    files = {'file': uploaded_file}
    response = requests.post("http://localhost:8000/predict", files=files)

    # Result ko display karne wala function
    if response.status_code == 200:
        result = response.json()["result"]
        st.markdown(f'<div style="background-color:#f0f0f0; padding:10px; border-radius:5px; font-size:18px;">{result}</div>', unsafe_allow_html=True)
    else:
        st.error("Error predicting the species. Please try again.")



# Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)