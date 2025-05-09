import Xulyanhso.Main
import streamlit as st

import pages.NhanDangTraiCay.nhan_dang_trai_cay as traicay
import pages.GiaiPTBac2.giai_phuong_trinh_bac_2 as gptb2
import pages.NhanDangChuSoMNist.predict_gui as mnist
import Xulyanhso


logo_url = "images/logo.png"

# === Sidebar ===
st.sidebar.image(logo_url, use_container_width=True)
st.sidebar.title("Xử Lý Ảnh Số")

# Khởi tạo session state
for key in ["selectbox_c3", "selectbox_c4", "selectbox_c9", "page"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# Hàm callback cho từng selectbox
def on_select_c3():
    st.session_state.selectbox_c4 = ""
    st.session_state.selectbox_c9 = ""
    st.session_state.page = ""

def on_select_c4():
    st.session_state.selectbox_c3 = ""
    st.session_state.selectbox_c9 = ""
    st.session_state.page = ""
def on_select_c9():
    
    st.session_state.selectbox_c3 = ""
    st.session_state.selectbox_c4 = ""
    st.session_state.page = ""

# Callback: khi chọn radio (chức năng)
def on_select_page():
    st.session_state.selectbox_c3 = ""
    st.session_state.selectbox_c4 = ""
    st.session_state.selectbox_c9 = ""

# Sidebar Radio (Chức năng)
st.sidebar.radio("📚 Danh sách nội dung: ", 
    ["", "Nhận dạng khuôn mặt", "Giải phương trình bậc 2", "Nhận dạng đối tượng", 
     "Nhận dạng trái cây", "Nhận dạng chữ số MNIST"], 
    key="page", on_change=on_select_page)

# Sidebar Selectbox cho từng chương
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

# === Trang chủ (Chỉ khi chưa chọn gì cả) ===
if st.session_state.page == "" and st.session_state.selectbox_c3 == "" and st.session_state.selectbox_c4 == "" and st.session_state.selectbox_c9 == "":
    st.title("Xử Lý Ảnh Số")
    st.markdown("""<div style='margin-left:1rem'>
                    <p>Lớp học phần : <strong>Xu ly anh so_ Nhom 07CLC</strong></p>
                    <p>GVHD : <strong>ThS. Trần Tiến Đức</strong></p>
                    <p>Sinh viên thực hiện : 
                    <p><strong>Phạm Thị Kim Ngân - 23110128</strong></p>
                    <p><strong>Nguyễn Thái Bình - 23110080</strong></p>
                  </div>""", unsafe_allow_html=True)


# === Các chức năng khác theo page ===
elif st.session_state.page == "Giải phương trình bậc 2":
    st.title("Giải phương trình bậc 2")
    gptb2.gptb2_page()
elif st.session_state.page == "Nhận dạng khuôn mặt":
    st.title("Nhận dạng 3 khuôn mặt")
    # khuonmat.nhan_dien()
elif st.session_state.page == "Nhận dạng đối tượng":
    st.title("Nhận dạng đối tượng")
    # doituong.nhan_dang_doi_tuong_page()
elif st.session_state.page == "Nhận dạng chữ số MNIST":
    st.title("Nhận dạng chữ số viết tay MNIST")
    mnist.nhan_dang_mnist()
elif st.session_state.page == "Nhận dạng trái cây":
    st.title("Nhận dạng 5 loại trái cây")
    traicay.nhan_dang_trai_cay_page()

# Xu ly anh so ---------------------------------
#Chuong3 -----------------------------------
elif st.session_state.selectbox_c3 == "Negative":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Negative Color":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Logarit":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Power":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Piecewise Line":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Histogram":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Hist Equal":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Hist Equal Color":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Local Hist":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Hist Stat":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Smooth Gauss":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Median Filter":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c3 == "Sharp":
    Xulyanhso.Main.Xulyanhso_page()

#Chuong4 -----------------------------------
elif st.session_state.selectbox_c4 == "Spectrum":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c4 == "Remove Moire":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c4 == "Remove Moire Butterworth":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c4 == "Remove Interference":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c4 == "Create Motion":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c4 == "DeMotion":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c4 == "DeMotion noise":
    Xulyanhso.Main.Xulyanhso_page()

#Chuong9 -----------------------------------
elif st.session_state.selectbox_c9 == "Connected Components":
    Xulyanhso.Main.Xulyanhso_page()
elif st.session_state.selectbox_c9 == "Remove Small Rice":
    Xulyanhso.Main.Xulyanhso_page()