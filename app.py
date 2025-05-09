import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Daily Line Chart", layout="wide")

st.title("📈 Daily Line Chart Viewer")

st.write("Upload a CSV file containing your line chart data.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Read the uploaded CSV
        df = pd.read_csv(uploaded_file)

        # Assume the first column is X-axis, rest are Y-axis series
        st.write("Preview of Data:")
        st.dataframe(df)

        st.write("Generated Line Chart:")

        # Plot the line chart
        fig, ax = plt.subplots(figsize=(10, 5))
        df.set_index(df.columns[0]).plot(ax=ax)
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel("Values")
        ax.set_title("Line Chart")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error reading file: {e}")
