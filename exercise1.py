import streamlit as st
from PIL import Imaage
x = st.slider("Select a value")
st.write(x, "squared is", x * x)


img = Image.open("image/a1.jpg")
st.image(img,width=200)

if st.checkbox("Show/Hide"):
  st.text("Showing the widget")
  st.image(img,width=50)

status = st.radio("select gender:", ('Male','Female'))
st.success(status)
