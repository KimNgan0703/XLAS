
import streamlit as st
import math

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

    def clear_input():
        st.session_state["nhap_a"] = 0.0
        st.session_state["nhap_b"] = 0.0
        st.session_state["nhap_c"] = 0.0

    st.subheader('Giải phương trình bậc 2')
    with st.form(key='columns_in_form', clear_on_submit=False):
        a = st.number_input('Nhập a', key='nhap_a')
        b = st.number_input('Nhập b', key='nhap_b')
        c = st.number_input('Nhập c', key='nhap_c')

        c1, c2 = st.columns(2)
        with c1:
            btn_giai = st.form_submit_button('Giải')
        with c2:
            btn_xoa = st.form_submit_button('Xóa', on_click=clear_input)

        if btn_giai:
            ket_qua = gptb2_tinh(a, b, c)
            st.markdown('Kết quả: ' + ket_qua)
        else:
            st.markdown('Kết quả:')