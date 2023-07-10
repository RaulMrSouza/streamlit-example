import cv2
import streamlit as st
import numpy as np
from PIL import Image

st.title('Detecção de Desfoque')

uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, use_column_width=True)

    if fm < 30:
        st.write(f'A imagem está desfocada. Nitidez: {round(fm,2)}')
    else:
        st.write(f'A imagem não está desfocada. Nitidez: {round(fm,2)}')
