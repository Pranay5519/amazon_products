import streamlit as st
import pandas as pd
path = r'C:\Users\HP\Desktop\amazon_product_data\new_to_amazon.csv'

df = pd.read_csv(path)
df = df.sample(frac=1)
df.dropna(inplace=True)

nu_rows = 5
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