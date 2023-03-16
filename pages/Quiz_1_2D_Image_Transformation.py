import numpy as np
import cv2
import matplotlib.pyplot as plt

i = int(1)
jpg = ".jpg"
img_ = cv2.imread(str(i) + jpg)
img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
cols, rows = img_.shape[:2]

m_translation_ = np.float32([[1, 0, 100],
                             [0, 1, 50],
                             [0, 0, 1]])
angle = np.radians(10)
m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                          [np.sin(angle), np.cos(angle), 0],
                          [0, 0, 1]])
m_scaling_ = np.float32([[1.5, 0, 0],
                         [0, 1.8, 0],
                         [0, 0, 1]])
m_reflection_ = np.float32([[1, 0, 0],
                            [0, -1, rows],
                            [0, 0, 1]])
m_shearing_x = np.float32([[1, 0.5, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

def translation(img_, cols, rows):
    for i in range(1, 6):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2]

        translated_img_ = cv2.warpPerspective(img_, m_translation_, (cols, rows))
        plt.axis('off')
        plt.imshow(translated_img_)
        plt.show()

def rotation(img_, cols, rows):
    for i in range(1, 6):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2]

        rotated_img_ = cv2.warpPerspective(img_, m_rotation_, (int(cols), int(rows)))
        plt.axis('off')
        plt.imshow(rotated_img_)
        plt.show()

def scaling(img_, cols, rows):
    for i in range(1, 6):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2]

        scaled_img_ = cv2.warpPerspective(img_, m_scaling_, (cols*2, rows*2))
        plt.axis('off')
        plt.imshow(scaled_img_)
        plt.show()

def reflection(img_, cols, rows):
    for i in range(1, 6):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2]

        reflected_img_ = cv2.warpPerspective(img_, m_reflection_, (int(cols), int(rows)))
        plt.axis('off')
        plt.imshow(reflected_img_)
        plt.show()    

def shear(img_, cols, rows):
    for i in range(1, 6):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2]

        sheared_img_x = cv2.warpPerspective(img_, m_shearing_x, (int(cols*1.5), int(rows*1.5)))
        plt.axis('off')
        plt.imshow(sheared_img_x)
        plt.show()

def main():
        translation(img_, cols, rows)
        rotation(img_, cols, rows)
        scaling(img_, cols, rows)
        reflection(img_, cols, rows)
        shear(img_, cols, rows)

if __name__ == "__main__":
    main()