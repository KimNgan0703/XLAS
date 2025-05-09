import streamlit as st
import cv2
import numpy as np
from Xulyanhso import Chapter3 as c3
from Xulyanhso import Chapter4 as c4
from Xulyanhso import Chapter9 as c9

st.set_page_config(page_title="Xử lý ảnh số", layout="wide")
# --- Nút làm mới ---
if st.button("🔄 Làm mới tất cả"):
    for key in ["c3", "c4", "c9", "uploaded_img"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# --- Khởi tạo session state ---
for key in ["selectbox_c3", "selectbox_c4", "selectbox_c9"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# --- Hàm callback cho từng selectbox ---
def on_select_c3():
    st.session_state.selectbox_c4 = ""
    st.session_state.selectbox_c9 = ""

def on_select_c4():
    st.session_state.selectbox_c3 = ""
    st.session_state.selectbox_c9 = ""

def on_select_c9():
    st.session_state.selectbox_c3 = ""
    st.session_state.selectbox_c4 = ""

# --- Sidebar ---
st.sidebar.selectbox("📘 Chapter 3", [
    "", "Negative", "Negative Color", "Logarit", "Power", "Piecewise Line", "Histogram",
    "Hist Equal", "Hist Equal Color", "Local Hist", "Hist Stat", "Smooth Gauss",
    "Median Filter", "Sharp"
], key="selectbox_c3", on_change=on_select_c3)

st.sidebar.selectbox("📗 Chapter 4", [
    "", "Spectrum", "Remove Moire", "Remove Moire Butterworth", "Remove Interference",
    "Create Motion", "DeMotion", "DeMotion noise"
], key="selectbox_c4", on_change=on_select_c4)

st.sidebar.selectbox("📙 Chapter 9", [
    "", "Connected Components", "Remove Small Rice"
], key="selectbox_c9", on_change=on_select_c9)

# --- MAIN ---
st.title("🎨 Ứng dụng xử lý ảnh số")

# Xác định thao tác đã chọn
operation_c3 = st.session_state.selectbox_c3
operation_c4 = st.session_state.selectbox_c4
operation_c9 = st.session_state.selectbox_c9

selected_chapter = ""
if operation_c3: selected_chapter = "c3"
if operation_c4: selected_chapter = "c4"
if operation_c9: selected_chapter = "c9"

# Nếu có thao tác được chọn
if selected_chapter:
    st.subheader("📂 Upload ảnh đầu vào")

    uploaded_file = st.file_uploader("Chọn ảnh bất kỳ (JPG, PNG, BMP, TIFF...)", type=["jpg", "jpeg", "png", "bmp", "tif", "tiff"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        imgin = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

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

        # --- Hiển thị kết quả ---
        if imgout is not None:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 📥 Ảnh gốc")
                st.image(imgin if imgin.ndim == 2 else cv2.cvtColor(imgin, cv2.COLOR_BGR2RGB))
            with col2:
                st.markdown("### 🎯 Ảnh đã xử lý")
                st.image(imgout if imgout.ndim == 2 else cv2.cvtColor(imgout, cv2.COLOR_BGR2RGB))

else:
    st.info("👉 Vui lòng chọn một chức năng xử lý ở thanh bên để bắt đầu.")
