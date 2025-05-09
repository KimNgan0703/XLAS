import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

def gptb2_page():
    def gptb2_tinh(a, b, c):
        if a == 0:
            if b == 0:
                if c == 0:
                    return 'PTB1 có vô số nghiệm'
                else:
                    return 'PTB1 vô nghiệm'
            else:
                x = -c / b
                return 'PTB1 có nghiệm %.2f' % x
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                return 'PTB2 vô nghiệm'
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                return 'PTB2 có nghiệm x1 = %.2f và x2 = %.2f' % (x1, x2)

    def plot_quadratic(a, b, c):
        # Tạo giá trị x, mở rộng phạm vi để hiển thị parabol rõ ràng hơn
        x = np.linspace(-100, 100, 400)
        # Tính giá trị y cho phương trình bậc hai y = ax^2 + bx + c
        y = a * x**2 + b * x + c
        
        # Tính giá trị y tối đa và tối thiểu để điều chỉnh phạm vi trục y động
        y_max = max(y)
        y_min = min(y)
        y_range = max(abs(y_max), abs(y_min)) * 1.2  # Mở rộng phạm vi trục y thêm 20% để dễ nhìn
        
        # Vẽ biểu đồ
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, color='blue', label=f'{a}x² + {b}x + {c}')
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Biểu đồ phương trình bậc 2')
        plt.legend()
        plt.ylim(-y_range, y_range)  # Điều chỉnh trục y động để hiển thị parabol rõ ràng
        
        # Lưu biểu đồ thành file
        plt.savefig('quadratic_plot.png')
        plt.close()
        return 'quadratic_plot.png'

    def clear_input():
        st.session_state["nhap_a"] = 0.0
        st.session_state["nhap_b"] = 0.0
        st.session_state["nhap_c"] = 0.0

    # Thêm một số kiểu dáng tùy chỉnh
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stNumberInput label {
            font-weight: bold;
            color: #333;
        }
        </style>
    """, unsafe_allow_html=True)

    st.subheader('Giải phương trình bậc 2')

    # Chia bố cục thành 2 cột: bên trái để nhập số, bên phải để hiển thị biểu đồ
    col1, col2 = st.columns([1, 1])

    with col1:
        with st.form(key='columns_in_form', clear_on_submit=False):
            a = st.number_input('Nhập a', key='nhap_a', step=0.01, format="%.2f")
            b = st.number_input('Nhập b', key='nhap_b', step=0.01, format="%.2f")
            c = st.number_input('Nhập c', key='nhap_c', step=0.01, format="%.2f")

            c1, c2 = st.columns(2)
            with c1:
                btn_giai = st.form_submit_button('Giải')
            with c2:
                btn_xoa = st.form_submit_button('Xóa', on_click=clear_input)

            if btn_giai:
                ket_qua = gptb2_tinh(a, b, c)
                st.markdown(f'**Kết quả:** {ket_qua}')
            else:
                st.markdown('**Kết quả:**')

    with col2:
        if btn_giai:
            if a != 0:  # Chỉ vẽ biểu đồ nếu là phương trình bậc hai
                plot_file = plot_quadratic(a, b, c)
                st.image(plot_file, caption='Biểu đồ phương trình', use_container_width=True)
            else:
                st.warning("Đây không phải là phương trình bậc 2, không thể vẽ biểu đồ.")
        else:
            st.markdown('**Biểu đồ:**')

# Chạy trang
gptb2_page()