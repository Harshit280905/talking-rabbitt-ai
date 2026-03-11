import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt — Conversational Analytics MVP")

st.write("Upload a sales CSV and ask questions about your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    question = st.text_input("Ask a question about the dataset")

    if question:

        if "region" in question.lower():

            revenue_by_region = df.groupby("Region")["Revenue"].sum()

            top_region = revenue_by_region.idxmax()
            top_value = revenue_by_region.max()

            st.success(f"The region with the highest revenue is {top_region} with {top_value}")

            fig, ax = plt.subplots()
            revenue_by_region.plot(kind="bar", ax=ax)

            st.pyplot(fig)

        elif "product" in question.lower():

            revenue_by_product = df.groupby("Product")["Revenue"].sum()

            top_product = revenue_by_product.idxmax()
            top_value = revenue_by_product.max()

            st.success(f"The top performing product is {top_product} with revenue {top_value}")

            fig, ax = plt.subplots()
            revenue_by_product.plot(kind="bar", ax=ax)

            st.pyplot(fig)

        else:
            st.warning("Try asking about regions or products.")
