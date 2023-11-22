import streamlit as st
import requests
import time
#Set background image using custom CSS
background_image = r"C:\ROHIT\CS\ML\projects\BDCOE-final\data\ele.jpg"
background_css = f"""
    <style>
        .stApp {{
            background-image: linear-gradient(
            to bottom,
            rgba(255, 255, 0, 0.5),
            rgba(0, 0, 255, 0.5)
            ), url("{background_image}");
            background-size: initial;
            
        }}
    </style>
"""
st.markdown(background_css, unsafe_allow_html=True)
st.title(":blue[⛔Endangered Animals🫏 Detection]")

uploaded_file = st.file_uploader("Choose a wildlife image...", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Upload image to the FastAPI backend
    files = {'file': uploaded_file}
    response = requests.post("http://localhost:8000/predict", files=files)

    # Display the result
    if response.status_code == 200:
        result = response.json()["result"]
        st.success(f"The species is classified as: {result}")
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