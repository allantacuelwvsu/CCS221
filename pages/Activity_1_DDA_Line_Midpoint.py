#ddaline
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Activity\t1\nGroup\t8\tBYTE\nDDA\tMidpoint")

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    x3 = ((x1 + x2) / 2)
    y3 = ((y1 + y2) / 2)

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xcoordinate = float(dx / steps)
    Ycoordinate = float(dy / steps)

    fig = plt.figure()
    for i in range(0, int(steps + 1)):

        print('x = %s, y = %s' % (x1, y1))
        plt.plot(int(x1), int (y1), color)
        x1 += Xcoordinate
        y1 += Ycoordinate
    plt.plot(x3, y3, marker = "o", markersize = 5, markerfacecolor = "red")
    plt.show()
    st.pyplot(fig)
    st.write("Midpoint: ", int(x3), ", ", int(y3), ".")

def main():
    st.title("DDA Line")

    x1 = st.slider(
        'x1',
        0, 100)

    y1 = st.slider(
        'y1',
        0, 100)

    x2 = st.slider(
        'x2',
        0, 100)

    y2 = st.slider(
        'y2',
        0, 100)
    color = "g." 
    DDALine(x1, y1, x2, y2, color)

if __name__ == '__main__':
    main()
