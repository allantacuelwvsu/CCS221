import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

fig = plt.figure()

def translation(img_):
    m_translation_ = np.float32([[1, 0, 100],
                                 [0, 1, 50],
                                 [0, 0, 1]])
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2]

    translated_img_ = cv2.warpPerspective(img_, m_translation_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(translated_img_)
    plt.show()
    st.pyplot(fig)

def rotation(img_):
    angle = np.radians(10)
    m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                              [np.sin(angle), np.cos(angle), 0],
                              [0, 0, 1]])
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2]

    rotated_img_ = cv2.warpPerspective(img_, m_rotation_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(rotated_img_)
    plt.show()
    st.pyplot(fig)

def scaling(img_):
    m_scaling_ = np.float32([[1.5, 0, 0],
                             [0, 1.8, 0],
                             [0, 0, 1]])
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2]

    scaled_img_ = cv2.warpPerspective(img_, m_scaling_, (cols*2, rows*2))
    plt.axis('off')
    plt.imshow(scaled_img_)
    plt.show()
    st.pyplot(fig)

def reflection(img_):
    m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]])
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2]

    reflected_img_ = cv2.warpPerspective(img_, m_reflection_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(reflected_img_)
    plt.show()    
    st.pyplot(fig)

def shear(img_):
    m_shearing_x = np.float32([[1, 0.5, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2]

    sheared_img_x = cv2.warpPerspective(img_, m_shearing_x, (int(cols*1.5), int(rows*1.5)))
    plt.axis('off')
    plt.imshow(sheared_img_x)
    plt.show()
    st.pyplot(fig)

def main():
    Transformation = st.multiselect('Choose Transformation Method', ['translation', 'rotation', 'scale', 'shear', 'reflection'])
    image_upload = st.file_uploader('Upload Image to Use', ['jpg'], accept_multiple_files=False)   
    if ('translation' in Transformation):
        translation(image_upload)
    if ('rotation' in Transformation):
        rotation(image_upload)
    if ('scale' in Transformation):
        scaling(image_upload)
    if ('shear' in Transformation):
        reflection(image_upload)
    if ('reflection' in Transformation):
            shear(image_upload)

if __name__ == "__main__":
    main()
