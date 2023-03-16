import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

st.title("Activity3\nGroup6\nImages")
# Reading of Image
jpg = str(".jpg")
fig = plt.figure()
address = str("C:/Users/admin/Desktop/PROG/python_acts/python_exercises/")

def translation(x,y,img_):
    
    #Translation
    m_translation_ = np.float32([[1, 0, x],
                                 [0, 1, y],
                                 [0, 0, 1]])
    
    
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2] 
    translated_image = cv2.warpPerspective(img_, m_translation_, (int(cols), int(rows)))
    
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)

def rotation(angle, img_):
    
    # Rotation
    angle = np.radians(angle)
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
    
def scaling(img_,xs,ys):
    
    # Scaling
    
    m_scaling_ = np.float32([[xs, 0, 0],
                             [0, ys, 0],
                             [0, 0, 1]])
    
   
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2] 

    scaled_img_ = cv2.warpPerspective(img_, m_scaling_, (cols*2, rows*2))
    plt.axis('off')
    plt.imshow(scaled_img_)
    plt.show()
    st.pyplot(fig)
    
def shear(img_,shearsize):
    
    # Shearing
    m_shearing_x = np.float32([[1, shearsize, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
    
    
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2]

    sheared_img_x = cv2.warpPerspective(img_,m_shearing_x,(int(cols*1.5), int(rows*1.5)))
    plt.axis('off')
    plt.imshow(sheared_img_x)
    plt.show()
    st.pyplot(fig)

def reflection(img_):
    
    # Reflection
    
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    cols, rows = img_.shape[:2]
    
    choice = st.selectbox('Image Position', ('Original', 'Flip Y', 'Flip X'))
    
    if choice == "Original":
        m_reflection_ = np.float32([[1, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 1]])
        
        
    elif choice == "Flip Y":
        m_reflection_ = np.float32([[1, 0, 0],
                                    [0, -1, rows],
                                    [0, 0, 1]])

        
    elif choice == "Flip X":
        m_reflection_ = np.float32([[-1, 0, cols],
                                    [0, 1, 0],
                                    [0, 0, 1]])
        
        
    reflected_img_ = cv2.warpPerspective(img_, m_reflection_,(int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(reflected_img_)
    plt.show()
    st.pyplot(fig)


def main():
    
    method = st.multiselect('Choose Transformation Method', ['Translation', 'Rotation', 'Scale', 'Shear', 'Reflection'])
    uploaded = st.file_uploader('Upload Image to Use', ['jpg'], accept_multiple_files=False)
    
    if 'Translation' in method:
        x = st.slider('X Translation', -100, 500, 1)
        y = st.slider('Y Translation', -100, 500, 1)
        st.write("Translation")
        translation(x,y,uploaded)
    
    if 'Rotation' in method:
        angle = st.slider('Rotation Size', -100, 500, 1)
        st.write("Rotation")
        rotation(angle,uploaded)
        
    if 'Scale' in method:
        xs = float(st.slider('X Translation', 0.0, 5.0, 0.000001))
        ys = float(st.slider('Y Translation', 0.0, 5.0, 0.000001))
        st.write("Scale")
        scaling(uploaded,xs,ys)
    
    if 'Shear' in method:
        shearsize = st.slider('Shear Size', 0.0, 5.0, 0.000001)
        st.write("Shear")
        shear(uploaded, shearsize)
    
    if 'Reflection' in method:
        st.write("Reflection")
        reflection(uploaded)
    
    
if __name__ == '__main__':
    main()
