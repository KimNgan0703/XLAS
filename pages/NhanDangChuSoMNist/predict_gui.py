import streamlit as st
import numpy as np 
import cv2 
import tensorflow as tf
from tensorflow.keras import datasets, models, optimizers
from PIL import Image, ImageTk

OPTIMIZER = tf.keras.optimizers.Adam()

# load model
model = tf.keras.models.load_model('pages/NhanDangChuSoMNist/digit_model.keras')

#data
(_, _), (X_test, _) = datasets.mnist.load_data()

# reshape
X_test = X_test.reshape((10000, 28, 28, 1))


def tao_anh_ngau_nhien():
    #  Tạo 100 số ngẫu nhiên nằm trong phạm vi [0, 9999]
    index = np.random.randint(0, 9999, 100)

    sample = np.zeros((100, 28, 28, 1))
    for i in range(0, 100):
        sample[i] = X_test[index[i]]

    # Tạo ảnh đê xem
    k=0
    image = np.zeros((10*28, 10*28), np.uint8)
    for i in range(0, 10):
        for j in range(0, 10):
            image[i*28:(i+1)*28, j*28:(j+1)*28] = sample[k,:,:,0]  
            k = k + 1
       
    color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(color_coverted) 
    return image_pil, sample/255.0


def predict(image_pil, data):
    # image_pil, data = tao_anh_ngau_nhien()
    # st.image(image_pil)

    ket_qua = model.predict(data, verbose = 0)
    chu_so = []
    for i in range(0, 100):
        x = np.argmax(ket_qua[i])
        chu_so.append(x)
    s = ''
    dem = 0 
    for x in chu_so:
        s = s + str(x) + ' '
        dem = dem + 1 
        if dem % 10 == 0: 
            s = s + '\n'
    return s


def nhan_dang_mnist():
    generate_button = st.button('Tạo ngẫu nhiên')
    predict_button = st.button('Dự đoán')

    global image_pil, data
    if generate_button:
        image_pil, data = tao_anh_ngau_nhien()
        st.image(image_pil)
    if predict_button:
        s=predict(image_pil, data)
        st.image(image_pil)
        st.header("Kết quả nhận diện:")
        st.text(s)

