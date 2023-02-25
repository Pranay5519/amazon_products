import streamlit as st
import pandas as pd
from PIL import Image
import requests

st.title("Amazon Product Recommendation")
data = pd.read_csv(r"C:\Users\HP\Desktop\amazon_product_data\amazon_product_data.csv")

categories = data['category'].unique().tolist()
cat_input = st.sidebar.selectbox('Categories' , categories)


if st.sidebar.button("Search"):
    st.empty()
    df = data[data['category'] ==cat_input]
    df.reset_index(inplace  = True)
    df = df.sort_values(['rating'])

    nu_rows = 10
    nu_col = 5

    x = 0
    for i in range(nu_rows):
        cols = st.columns(nu_col)
        for j in range(nu_col):

            cols[j].image(df['link'][x])

            cols[j].caption(df['title'][x])
            cols[j].write(df['rating'][x])
            cols[j].subheader(f"Rs:-{df['price'][x]}")
            x+=1






