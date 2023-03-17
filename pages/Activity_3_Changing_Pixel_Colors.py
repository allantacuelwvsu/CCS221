import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Activity\t3\nGroup\t8\tBYTE\nAxes")

fig = plt.figure()
two_d_arr = np.array([[1.0, 0.0, 1.0],
                      [0.0, 0.0, 0.0],
                      [1.0, 0.0, 1.0]])

def main():

        st.title("Colormap")

        choice = st.slider(
                 'Map',
                 1, 3)
        st.write('Map: ', choice)
    
        st.title("Coordinates and Color to Replace")

        colorchange = st.slider(
            'New Color',
            0.0, 1.0)
        st.write('Color: ', colorchange)
        row = st.slider(
            'Y',
            0, 2)
        st.write('Y: ', row)
        column = st.slider(
            'X',
            0, 2)
        st.write('X: ', column)
        two_d_arr[row][column] = colorchange
        
        if (choice == 1):
            plt.imshow(two_d_arr, interpolation = 'none', cmap = 'plasma')
        elif (choice == 2):
            plt.imshow(two_d_arr, interpolation = 'none', cmap = 'gray_r')
        elif (choice == 3):
            plt.imshow(two_d_arr, interpolation = 'none', cmap = 'inferno')
        plt.colorbar()
        st.pyplot(fig)
        plt.colorbar()
        plt.show()


if __name__ == '__main__':
    main()
