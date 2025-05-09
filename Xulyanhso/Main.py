import streamlit as st
import numpy as np
import cv2

from Xulyanhso import Chapter3 as c3
from Xulyanhso import Chapter4 as c4
from Xulyanhso import Chapter9 as c9

def process_image(selected_chapter, operation_c3, operation_c4, operation_c9, file_bytes):
    # Chuyển đổi ảnh từ byte thành ndarray
    imgin = np.asarray(bytearray(file_bytes), dtype=np.uint8)
    imgin = cv2.imdecode(imgin, cv2.IMREAD_UNCHANGED)

    if imgin.ndim == 3 and imgin.shape[2] == 4:
        imgin = cv2.cvtColor(imgin, cv2.COLOR_BGRA2BGR)

    if len(imgin.shape) == 2:
        gray_img = imgin.copy()
    else:
        gray_img = cv2.cvtColor(imgin, cv2.COLOR_BGR2GRAY)

    imgout = None

    # --- Chapter 3 ---
    if selected_chapter == "c3":
        if operation_c3 == "Negative":
            imgout = c3.Negative(gray_img)
        elif operation_c3 == "Negative Color":
            imgout = c3.NegativeColor(imgin)
        elif operation_c3 == "Logarit":
            imgout = c3.Logarit(gray_img)
        elif operation_c3 == "Power":
            imgout = c3.Power(gray_img)
        elif operation_c3 == "Piecewise Line":
            imgout = c3.PiecewiseLine(gray_img)
        elif operation_c3 == "Histogram":
            imgout = c3.Histogram(gray_img)
        elif operation_c3 == "Hist Equal":
            imgout = cv2.equalizeHist(gray_img)
        elif operation_c3 == "Hist Equal Color":
            imgout = c3.HisEqualColor(imgin)
        elif operation_c3 == "Local Hist":
            imgout = c3.LocalHist(gray_img)
        elif operation_c3 == "Hist Stat":
            imgout = c3.HistStat(gray_img)
        elif operation_c3 == "Smooth Gauss":
            imgout = cv2.GaussianBlur(gray_img, (43, 43), 7.0)
        elif operation_c3 == "Median Filter":
            imgout = cv2.medianBlur(gray_img, 5)
        elif operation_c3 == "Sharp":
            imgout = c3.Sharp(gray_img)

    # --- Chapter 4 ---
    elif selected_chapter == "c4":
        if operation_c4 == "Spectrum":
            imgout = c4.Spectrum(gray_img)
        elif operation_c4 == "Remove Moire":
            imgout = c4.RemoveMoire(gray_img)
        elif operation_c4 == "Remove Moire Butterworth":
            imgout = c4.RemoveMoireButterworth(gray_img)
        elif operation_c4 == "Remove Interference":
            imgout = c4.RemoveInterference(gray_img)
        elif operation_c4 == "Create Motion":
            imgout = c4.CreateMotion(gray_img)
        elif operation_c4 == "DeMotion":
            imgout = c4.DeMotion(gray_img)
        elif operation_c4 == "DeMotion noise":
            temp = cv2.medianBlur(gray_img, 7)
            imgout = c4.DeMotion(temp)

    # --- Chapter 9 ---
    elif selected_chapter == "c9":
        if operation_c9 == "Connected Components":
            imgout = c9.ConnectedCompoments(gray_img)
        elif operation_c9 == "Remove Small Rice":
            imgout = c9.RemoveSmallRice(gray_img)

    return imgout

def Xulyanhso_page():
    # === Nếu chọn xử lý ảnh số theo chương ===
    operation_c3 = st.session_state.selectbox_c3
    operation_c4 = st.session_state.selectbox_c4
    operation_c9 = st.session_state.selectbox_c9
    selected_chapter = ""
    if operation_c3: selected_chapter = "c3"
    if operation_c4: selected_chapter = "c4"
    if operation_c9: selected_chapter = "c9"

    if selected_chapter:
        st.header("📂 Upload ảnh đầu vào")
        if st.button("🔄 Làm mới tất cả"):
            for key in ["uploaded_file"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

        uploaded_file = st.file_uploader("Chọn ảnh bất kỳ (JPG, PNG, BMP, TIFF...)", type=["jpg", "jpeg", "png", "bmp", "tif", "tiff"])

        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            imgout = process_image(selected_chapter, operation_c3, operation_c4, operation_c9, file_bytes)

            if imgout is not None:
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### 📥 Ảnh gốc")
                    st.image(file_bytes)
                with col2:
                    st.markdown("### 🎯 Ảnh đã xử lý")
                    st.image(imgout)
