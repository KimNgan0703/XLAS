import numpy as np
import cv2

L = 256
def FrequencyFiltering(imgin, H):
    f = imgin.astype(np.float32)
    # buoc1:DFT
    F = np.fft.fft2(f)
    # buoc2:Shift vao the center of of the image
    F = np.fft.fftshift(F)
    # Buoc 3:Nhan F voiw H
    G = F * H
    # Buoc 4: Shift return
    G =np.fft.ifftshift(G)
    # Buoc 5: IDFT
    g = np.fft.ifft2(G)
    gR =np.clip(g.real, 0, L -1)
    imgout = gR.astype(np.uint8)
    return imgout

def Spectrum(imgin):
    f = imgin.astype(np.float32)/(L-1)
    # buoc1:DFT
    F = np.fft.fft2(f)
    # buoc2:Shift vao the center of of the image
    F = np.fft.fftshift(F)

    # Buoc 5 - tính spectrum
    S = np.sqrt(F.real**2 + F.real**2)
    S = np.clip(S, 0, L-1)
    imgout = S.astype(np.uint8)
    return imgout



################################################
def CreateNotchFilter(M, N):
    # Tạo bộ lọc H là số phức, có phần ảo bằng 0
    H = np.zeros((M,N), np.complex64)
    H.imag = 0.0 

    u1, v1 = 45, 59
    u2, v2 = 86, 59
    u3, v3 = 39, 119
    u4, v4 = 83, 119

    u5, v5 = M-45, N-59
    u6, v6 = M-86, N-59
    u7, v7 = M-39, N-119
    u8, v8 = M-83, N-119
    D0 = 10
    for u in range(0, M):
        for v in range(0, N):
            # u1, v1            
            Duv = np.sqrt((u-u1)**2 + (v-v1)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0
            # u2, v2            
            Duv = np.sqrt((u-u2)**2 + (v-v2)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0
            # u3, v3            
            Duv = np.sqrt((u-u3)**2 + (v-v3)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0
            # u4, v4            
            Duv = np.sqrt((u-u4)**2 + (v-v4)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0

            # ######################
             # u5, v5            
            Duv = np.sqrt((u-u5)**2 + (v-v5)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0
            # u6, v6            
            Duv = np.sqrt((u-u6)**2 + (v-v6)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0
            # u7, v7            
            Duv = np.sqrt((u-u7)**2 + (v-v7)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0
            # u8, v8            
            Duv = np.sqrt((u-u8)**2 + (v-v8)**2)
            if Duv <= D0:
                H.real[u,v] = 0.0
    return H


def CreateMoireButterworthFilter(M, N):
     # Tạo bộ lọc H là số phức, có phần ảo bằng 0
    H = np.zeros((M,N), np.complex64)
    H.imag = 0.0 

    u1, v1 = 45, 59
    u2, v2 = 86, 59
    u3, v3 = 39, 119
    u4, v4 = 83, 119

    u5, v5 = M-45, N-59
    u6, v6 = M-86, N-59
    u7, v7 = M-39, N-119
    u8, v8 = M-83, N-119
    D0 = 10
    n=4
    for u in range(0, M):
        for v in range(0, N):
            # u1, v1      
            r = 1.0      
            Duv = np.sqrt((u-u1)**2 + (v-v1)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0
            # u2, v2            
            Duv = np.sqrt((u-u2)**2 + (v-v2)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0
            # u3, v3            
            Duv = np.sqrt((u-u3)**2 + (v-v3)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0
            # u4, v4            
            Duv = np.sqrt((u-u4)**2 + (v-v4)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0

            # ######################
             # u5, v5            
            Duv = np.sqrt((u-u5)**2 + (v-v5)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0
            # u6, v6            
            Duv = np.sqrt((u-u6)**2 + (v-v6)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0
            # u7, v7            
            Duv = np.sqrt((u-u7)**2 + (v-v7)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0
            # u8, v8            
            Duv = np.sqrt((u-u8)**2 + (v-v8)**2)
            if Duv <= D0:
                if Duv >= 1e-10:
                    r = r * 1.0/(1.0 + np.power(D0/Duv, n))
                else:
                    r = 0.0
            H.real[u,v] = r
    return H


def CreateInterferenceFilter(M, N):
    # Tạo bộ lọc H là số phức, có phần ảo bằng 0
    H = np.zeros((M, N), np.complex64)
    H.imag = 0.0
    D0 = 7
    D1 = 7
    for u in range(0, M):
        for v in range(0, N):
            if u not in range(M//2-D0, N//2+D0): 
                D = v-M//2
                if abs(D) <= D1:
                    H.real[u,v] = 0
    return H

def CreateMotionFilter(M, N):
    # Tạo bộ lọc H là số phức, có phần ảo bằng 0
    H = np.zeros((M, N), np.complex64)
    a = 0.1
    b = 0.1
    T = 1.0
    phi_prev =0.0
    for u in range(0,M):
        for v in range(0, N):
            phi = np.pi*((u- M//2)*a + (v- N//2)*b)
            if abs(phi) < 1.0e-6:
                phi = phi_prev
            RE = T*np.sin(phi)/phi*np.cos(phi)
            IM = T*np.sin(phi)/phi*np.sin(phi)
            H.real[u,v] = RE
            H.imag[u,v] = IM
    return H

def DeMotionFilter(M, N):
    # Tạo bộ lọc H là số phức
    H = np.zeros((M, N), np.complex64)
    a = 0.1
    b = 0.1
    T = 1.0
    phi_prev  = 0.0 
    for u in range(0, M):
        for v in range(0, N):
            phi = np.pi*((u-M//2)*a + (v-N//2)*b)
            mau_so = np.sin(phi)
            if abs(mau_so) < 1.0e-6:
                phi = phi_prev
            RE = phi/(T*np.sin(phi))*np.cos(phi)
            IM = phi/T
            H.real[u, v] = RE
            H.imag[u, v] = IM
            phi_prev = phi              
    return H

def RemoveMoire(imgin):
    M, N = imgin.shape
    H = CreateNotchFilter(M, N)
    imgout = FrequencyFiltering(imgin, H) 
    return imgout

def RemoveMoireButterworth(imgin):
    M, N = imgin.shape
    H = CreateMoireButterworthFilter(M, N)
    imgout = FrequencyFiltering(imgin, H) 
    return imgout

def RemoveInterference(imgin):
    M, N = imgin.shape
    H = CreateInterferenceFilter(M, N)
    imgout = FrequencyFiltering(imgin, H) 
    return imgout


def CreateMotion(imgin):
    M, N = imgin.shape
    H = CreateMotionFilter(M, N)
    imgout = FrequencyFiltering(imgin, H) 
    return imgout

def DeMotion(imgin):
    M, N = imgin.shape
    H = DeMotionFilter(M, N)
    imgout = FrequencyFiltering(imgin, H) 
    return imgout
     