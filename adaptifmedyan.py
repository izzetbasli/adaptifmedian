import numpy as np
import cv2
img=cv2.imread('enver_pasa.jpg',0)
def padding(img):
    b=np.zeros((img.shape[0],1))
    e=np.zeros((1,img.shape[1]+2))
    c=np.append(img,b,axis=1)
    d=np.append(b,c,axis=1)
    f=np.append(d,e,axis=0)
    padding=np.append(e,f,axis=0)
    return padding
def gurultu(image):
    s_vs_p = 0.5
    amount = 0.5
    out = np.copy(image)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[coords] = 1
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[coords] = 0
    return out
def filtre_olustur(img,orjinal_resim,filtre_boyutu='3x3'):
    cikis=np.copy(img)
    if filtre_boyutu=='3x3':
        pad = padding(orjinal_resim)
        for i in range(1,img.shape[0]+1):
            for j in range(1,img.shape[1]+1):
                matris=pad[i-1:i+2,j-1:j+2]
                cikis[i-1,j-1]=np.median(matris)
    if filtre_boyutu=='5x5':
        pad = padding(padding(orjinal_resim))
        for i in range(2,img.shape[0]+2):
            for j in range(2,img.shape[1]+2):
                matris=pad[i-2:i+3,j-2:j+3]
                cikis[i-2,j-2]=np.median(matris)
    if filtre_boyutu=='7x7':
        pad = padding(padding(padding(orjinal_resim)))
        for i in range(3,img.shape[0]+3):
            for j in range(3,img.shape[1]+3):
                matris=pad[i-3:i+4,j-3:j+4]
                cikis[i-3,j-3]=np.median(matris)
    if filtre_boyutu=='9x9':
        pad = padding(padding(padding(padding(orjinal_resim))))
        for i in range(4,img.shape[0]+4):
            for j in range(4,img.shape[1]+4):
                matris=pad[i-4:i+5,j-4:j+5]
                cikis[i-4,j-4]=np.median(matris)
    if filtre_boyutu=='11x11':
        pad = padding(padding(padding(padding(padding(orjinal_resim)))))
        for i in range(5,img.shape[0]+5):
            for j in range(5,img.shape[1]+5):
                matris=pad[i-5:i+6,j-5:j+6]
                cikis[i-5,j-5]=np.median(matris)
    return cikis
gurultulu=gurultu(img)
resim=filtre_olustur(gurultulu,img,'7x7')
cv2.imshow('cikis',resim)
cv2.imshow('giris',patates)
cv2.waitKey(0)