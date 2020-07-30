import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("matplotlib 畫圖")
st.markdown(r"畫一個 $\dfrac{\sin(x)}{x}")

X = np.linspace(-10,10,200)
Y = np.sinc(X)
plt.plot(X,Y);
st.pyplot()
