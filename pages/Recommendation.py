import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

def print_first_row(group):
    return group.iloc[[0]]


data = pd.read_csv("recommendation_data_amazon.csv")
del data['Unnamed: 0']


st.title("Product Recommendation Using Product ID")
product_id_ = data['asin'].unique().tolist()
product_id = st.sidebar.selectbox("Product ID's" , product_id_)



if st.sidebar.button("Recommend"):
    # recommending products using productid

    category = data[data['asin'] == product_id]['category']
    df = data[data['category'] == category.iloc[0]]
    # grouping by asin and selecting the first row of all groups
    grouped_df = df.groupby('asin')
    grouped_df = grouped_df.apply(print_first_row)
    grouped_df = grouped_df.sample(frac=1)

    x = 0
    cols = [f"col_{i}" for i in range(5)]
    cols = st.columns(len(cols))
    for col in cols:
        with col:
            st.image(grouped_df['image'][x])
            st.caption(grouped_df['title'][x])
            st.write(grouped_df['rating'][x])
            st.subheader(f"Rs:{grouped_df['price'][x]}")

        x+=1
